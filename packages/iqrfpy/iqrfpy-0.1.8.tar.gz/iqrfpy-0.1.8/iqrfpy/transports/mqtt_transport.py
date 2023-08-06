from dataclasses import dataclass
import json
import random
import string

from typing import Callable, Optional
from paho.mqtt.client import Client
from iqrfpy.messages.requests.irequest import IRequest
from iqrfpy.messages.responses.confirmation import Confirmation
from iqrfpy.messages.responses.iresponse import IResponse
from iqrfpy.transports.itransport import ITransport
from iqrfpy.messages.response_factory import ResponseFactory
from typeguard import typechecked

__all__ = (
    'MqttTransportParams'
    'MqttTransport'
)


@dataclass
@typechecked
class MqttTransportParams:
    host: str = 'localhost'
    port: int = 1883
    client_id: str = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(16))
    user: str = None
    password: str = None
    request_topic: str = None
    response_topic: str = None
    qos: int = 1
    keepalive: int = 60

    def __post_init__(self):
        if not (1024 <= self.port <= 65535):
            raise MqttParamsError('Port value should be between 1024 and 65535.')
        if (self.user is not None and self.password is None) or (self.user is None and self.password is not None):
            raise MqttParamsError('Both user and password parameters need to be specified, or neither of them.')
        if not (0 <= self.qos <= 2):
            raise MqttParamsError('QoS value should be between 0 and 2.')


class MqttTransport(ITransport):

    __slots__ = '_client', '_params', '_callback', '_sync', '_timeout'

    def __init__(self, params: MqttTransportParams, synchronous: bool = False, callback: Optional[Callable] = None,
                 auto_init: bool = False, timeout: Optional[int] = None):
        self._client: Optional[Client] = None
        self._params: MqttTransportParams = params
        self._sync: bool = synchronous
        self._callback: Optional[Callable] = callback
        self._timeout: Optional[int] = timeout
        self._msg_id: Optional[str] = None
        if auto_init:
            self.initialize()

    def initialize(self) -> None:
        self._client = Client(self._params.client_id)
        self._client.on_connect = self._connect_callback
        self._client.on_message = self._message_callback
        if self._params.user is not None and self._params.password is not None:
            self._client.username_pw_set(self._params.user, self._params.password)
        self._client.connect(self._params.host, self._params.port)
        if not self._sync:
            self._client.loop_forever()

    def _connect_callback(self, client, userdata, flags, rc):
        # pylint: disable=W0613
        if rc == 0:
            self._client.subscribe(self._params.response_topic, self._params.qos)

    def _message_callback(self, client, userdata, message):
        # pylint: disable=W0613
        payload = json.loads(message.payload.decode('utf-8'))
        response = ResponseFactory.get_response_from_json(payload)
        if self._callback is not None:
            self._callback(response)

    def send(self, request: IRequest) -> None:
        if self._client.is_connected():
            self._client.publish(
                topic=self._params.request_topic,
                payload=json.dumps(request.to_json()),
                qos=self._params.qos
            )
            if self._sync:
                self._msg_id = request.get_msg_id()

    def send_and_receive(self, request: IRequest, timeout: Optional[int] = None) -> IResponse:
        pass

    def confirmation(self) -> Confirmation:
        raise NotImplementedError('Method not implemented.')

    def set_receive_callback(self, callback: Callable[[IResponse], None]) -> None:
        self._callback = callback


class MqttParamsError(Exception):
    pass
