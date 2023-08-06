from collections import namedtuple
from time import sleep
from traceback import format_exc
from typing import Optional, Callable, List, Generator

from pika.exceptions import AMQPError
from pika.exchange_type import ExchangeType
from typeguard import typechecked

from robotnikmq.config import RobotnikConfig
from robotnikmq.core import Robotnik, ConnErrorCallback, Message
from robotnikmq.error import MalformedMessage
from robotnikmq.log import log

OnMessageCallback = Callable[[Message], None]

ExchangeBinding = namedtuple("ExchangeBinding", ["exchange", "binding_key"])


class Subscriber(Robotnik):
    TIMEOUT_MAX = 30
    TIMEOUT_MIN = 1
    TIMEOUT_STEP = 3

    @typechecked
    def __init__(
        self,
        exchange_bindings: Optional[List[ExchangeBinding]] = None,
        config: Optional[RobotnikConfig] = None,
        on_conn_error: ConnErrorCallback = None,
    ):
        super().__init__(config=config, on_conn_error=on_conn_error)
        self.exchange_bindings = exchange_bindings or []

    @typechecked
    def _bind(self, exchange_binding: ExchangeBinding) -> "Subscriber":
        self.exchange_bindings.append(exchange_binding)
        return self

    @typechecked
    def bind(self, exchange: str, binding_key: str = "#") -> "Subscriber":
        return self._bind(ExchangeBinding(exchange, binding_key))

    @typechecked
    def _consume(
        self, inactivity_timeout: Optional[float]
    ) -> Generator[Optional[Message], None, None]:
        with self.open_channel() as channel:
            queue_name = (
                channel.queue_declare(queue="", exclusive=True).method.queue or ""
            )
            for ex_b in self.exchange_bindings:
                channel.exchange_declare(
                    exchange=ex_b.exchange,
                    exchange_type=ExchangeType.topic,
                    auto_delete=True,
                )
                channel.queue_bind(
                    exchange=ex_b.exchange,
                    queue=queue_name,
                    routing_key=ex_b.binding_key,
                )
            try:
                for method, ___, body in channel.consume(
                    queue=queue_name,  # pragma: no cover
                    auto_ack=False,
                    inactivity_timeout=inactivity_timeout,
                ):
                    if method and body:
                        channel.basic_ack(delivery_tag=method.delivery_tag or 0)
                        try:
                            yield Message.of(body.decode())
                        except MalformedMessage:
                            log.debug(format_exc())
                    else:
                        yield None
            finally:
                try:
                    channel.cancel()
                    self.close_channel(channel)
                except AssertionError as exc:
                    log.warning(f"Unable to close channel: {exc}")

    @typechecked
    def consume(
        self, inactivity_timeout: Optional[float] = None
    ) -> Generator[Optional[Message], None, None]:
        timeout = Subscriber.TIMEOUT_MIN
        while 42:
            try:
                for msg in self._consume(inactivity_timeout):
                    yield msg
                    timeout = Subscriber.TIMEOUT_MIN
            except (AMQPError, OSError) as exc:
                log.warning(f"Subscriber issue encountered: {exc}")
                timeout = min(timeout + Subscriber.TIMEOUT_STEP, Subscriber.TIMEOUT_MAX)
                log.warning(f"Backing off for {timeout} seconds before reconnecting...")
                sleep(timeout)
                log.warning("Reconnecting")
