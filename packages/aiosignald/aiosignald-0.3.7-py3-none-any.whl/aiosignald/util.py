from dataclasses import dataclass, is_dataclass, asdict
import asyncio
import dataclasses
import json
import logging
import typing
import types
from uuid import uuid4

from . import generated
from . import exc


class SignaldException(Exception):
    """
    Base class to translate signald's response payloads into python exceptions
    """

    def __init__(self, payload):
        self.payload = payload

    def __str__(self):
        return f"{self.__class__.__name__}: {self.payload}"


class SignaldUnlistedException(SignaldException):
    pass


@dataclass
class Handler:
    """
    Allows to await for a specific message sent by JSONProtocol.
    This should not be used directly, but rather using
    JSONProtocol.get_future_for(validator).

    :param validator: a Callable that will receive the response and return True
        if the response is the one it was waiting for
    :param callback: a Callable that will be called with the response as argument
    """

    validator: typing.Callable
    callback: typing.Callable

    def validate(self, response):
        return self.validator(response)


class JSONProtocol(asyncio.Protocol):
    PROTOCOL_VERSION = "v1"

    def __init__(self, on_con_lost: typing.Optional[asyncio.Future] = None):
        """
        :param on_con_lost: its result will be set to True once the connection is lost
            If not given, will be automatically generated.
        """
        self._buffer = bytearray()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.transport: typing.Optional[asyncio.transports.Transport] = None

        if on_con_lost is None:
            on_con_lost = asyncio.get_running_loop().create_future()

        self.on_con_lost = on_con_lost
        self.callbacks: dict[str, typing.Callable[[dict], dict]] = {}
        self.specific_handlers: list[Handler] = []

    def connection_made(self, transport: asyncio.transports.BaseTransport):
        if not isinstance(transport, asyncio.transports.Transport):
            raise RuntimeError("Transport must be R/W")
        self.logger.info("Connection established")
        self.transport = transport

    def connection_lost(self, exc: typing.Union[Exception, None]):
        self.logger.info(f"Connection lost: {exc}")
        self.transport = None
        try:
            self.on_con_lost.set_result(True)
        except asyncio.InvalidStateError:
            pass

    def data_received(self, data: bytes):
        """
        Handle data received through the UNIX socket, convert it to a python
        dict and dispatch it to the relevant callback or handler.

        Callbacks can either:

        - wait for a specific payload id, for this you should use the coroutine
          JSONProtocol.get_response
        - wait for a more generic matching payload, for this you should use the
          coroutine JSONProtocol.get_future_for

        In case no callbacks match the payload, it is sent to the method
        JSONProtocol.handle_{payload.type}.

        """
        buffer = self._buffer
        buffer += data
        if not buffer.endswith(b"\n"):
            return

        data = buffer
        self._buffer = bytearray()

        for line in data.decode("utf-8").split("\n"):
            if not line:
                continue  # Empty lines are sometimes sent apparently…

            payload = json.loads(line)
            if self.logger.isEnabledFor(logging.DEBUG):
                self.logger.debug(
                    "Received payload:"
                    + "\n"
                    + json.dumps(payload, indent=4, sort_keys=True)
                )

            for handler in self.specific_handlers:
                if handler.validate(payload):
                    self.logger.debug("Found a specific handler")
                    self.specific_handlers.remove(handler)
                    handler.callback(payload)
                    return

            id_ = payload.get("id")
            if id_ is None:
                type_ = payload.get("type")
                try:
                    generic_handler: typing.Callable = getattr(self, f"handle_{type_}")
                except AttributeError:
                    self.logger.info(f"No method to handle {type_}, ignoring")
                    return
                self.logger.debug(
                    "Method found to handle '%s': %s", type_, generic_handler
                )

                try:
                    attr = getattr(generated, type_ + self.PROTOCOL_VERSION)
                except AttributeError:
                    self.logger.warning(
                        "No dataclass for: %s, passing raw JSON payload", type_
                    )
                    data = payload
                else:
                    self.logger.debug("Found: %s", attr)
                    data = dict_to_nested_dataclass(attr, payload["data"])

                try:
                    if asyncio.iscoroutinefunction(generic_handler):
                        asyncio.create_task(self.__wrap(generic_handler, data, payload))
                    else:
                        generic_handler(data, payload)
                except Exception as e:
                    self.exception(generic_handler, e)
            else:
                callback = self.callbacks.pop(id_, None)
                if callback is None:
                    self.logger.warning(
                        "Received payload with id but no callbacks were"
                        "registered for it, ignoring"
                    )
                else:
                    callback(payload)

    async def __wrap(
        self,
        handler: typing.Callable[[typing.Any, dict], typing.Awaitable[None]],
        data: typing.Any,
        payload: dict,
    ):
        try:
            await handler(data, payload)
        except Exception as e:
            self.exception(handler, e)

    def exception(self, handler: typing.Callable, e: Exception):
        """
        Handle exceptions in generic handlers

        Override this function or set the attribute to customize the default
        behaviour, which is to just log the exception
        """
        self.logger.exception("Exception in %s", handler, exc_info=e)

    def send_request(
        self,
        payload: dict,
        id_: typing.Optional[str] = None,
        callback: typing.Optional[typing.Callable] = None,
    ):
        """
        Send a JSON payload to the UNIX socket.

        :param payload: dict
        :param id_: identifier of the request. If not specified, a random string is used.
        :param callback: a Callable that will be called with the response payload
        """
        if self.transport is None:
            self.logger.warning("No transport, cannot send payload")
            return

        if id_ is None:
            id_ = str(uuid4())
        payload["id"] = id_
        payload["version"] = self.PROTOCOL_VERSION

        if callback is not None:
            self.callbacks[id_] = callback

        if self.logger.isEnabledFor(logging.DEBUG):
            self.logger.debug(
                "Send payload" + "\n" + json.dumps(payload, indent=4, sort_keys=True)
            )
        self.transport.write(json.dumps(payload).encode("utf8") + b"\n")

    async def get_response(self, payload: dict, full: bool = False) -> dict:
        """
        Coroutine to await the response to a specific payload.
        Can raise exceptions in case the response is an error.

        :param payload:
        :param full: If False, return only payload["data"]
        """
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        self.send_request(payload=payload, callback=lambda p: future.set_result(p))
        response = await future
        raise_if_needed(response)
        if full:
            return response
        else:
            return response.get("data", dict())

    def handle_version(self, _data, payload):
        # special case where the event type does not correspond to the proper structure
        # version vs JsonVersionMessage
        return self.handle_JsonVersionMessage(
            generated.JsonVersionMessagev1(**payload["data"])
        )

    def handle_JsonVersionMessage(self, version):
        self.logger.info("Signald version: %s", version)


def locals_to_request(d: dict):
    """
    Helper for the generated bindings.
    """
    request: dict[str, typing.Any] = {}
    for k, v in d.items():
        if v is None or k == "self":
            continue
        if k == "async_":
            k = "async"
        k = k.replace("-", "_")
        if is_dataclass(v):
            request[k] = asdict(v)
        elif isinstance(v, (list, tuple)) and is_dataclass(v[0]):
            request[k] = [asdict(x) for x in v]
        else:
            request[k] = v
    return request


T = typing.TypeVar("T")


def evaluate_string_or_forward_ref(t: typing.Any):
    if isinstance(t, str):
        return getattr(generated, t)
    elif isinstance(t, typing.ForwardRef):
        return t._evaluate(generated.__dict__, locals(), frozenset())  # type:ignore
    else:
        return t


def dict_to_nested_dataclass(cls: typing.Type[T], dikt) -> T:
    kwargs = {}
    for field in dataclasses.fields(cls):  # type:ignore
        name = field.name

        dict_value = dikt.get(name)
        if dict_value is None:
            continue

        if isinstance(field.type, types.GenericAlias):
            type_ = field.type
        else:  # Non-lists are all Optional[...]
            type_ = evaluate_string_or_forward_ref(typing.get_args(field.type)[0])

        if is_dataclass(type_):
            kwargs[name] = dict_to_nested_dataclass(type_, dict_value)
        elif isinstance(type_, types.GenericAlias):
            # only works if GenericAlias is a list, but that's the case in this API
            nested_type = evaluate_string_or_forward_ref(typing.get_args(type_)[0])
            if is_dataclass(nested_type):
                kwargs[name] = [
                    dict_to_nested_dataclass(nested_type, x) for x in dict_value
                ]
            else:
                kwargs[name] = dict_value
        else:
            kwargs[name] = dict_value
    return cls(**kwargs)


def raise_if_needed(response: dict):
    """
    Raise a python exception using a signald response payload
    """
    if "error_type" in response:
        try:
            exc_cls = getattr(exc, response["error_type"])
        except AttributeError:
            raise SignaldUnlistedException(response)
        else:
            raise exc_cls(response["error"])


_FIELDS = "__dataclass_fields__"
