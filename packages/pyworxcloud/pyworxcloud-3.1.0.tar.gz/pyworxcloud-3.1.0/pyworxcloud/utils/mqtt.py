"""MQTT information class."""
from __future__ import annotations

import json
import random
import ssl
import urllib.parse
from datetime import datetime
from logging import Logger
from typing import Any
from uuid import uuid4

import paho.mqtt.client as mqtt
from paho.mqtt.client import connack_string

from ..events import EventHandler
from .landroid_class import LDict


class MQTTMsgType(LDict):
    """Define specific message type data."""

    def __init__(self) -> dict:
        super().__init__()

        self["in"] = 0
        self["out"] = 0


class MQTTMessageItem(LDict):
    """Defines a MQTT message for Landroid Cloud."""

    def __init__(
        self, device: str, data: str = "{}", qos: int = 0, retain: bool = False
    ) -> dict:
        super().__init__()

        self["device"] = device
        self["data"] = data
        self["qos"] = qos
        self["retain"] = retain


class MQTTMessages(LDict):
    """Messages class."""

    def __init__(self) -> dict:
        super().__init__()

        self["raw"] = MQTTMsgType()
        self["filtered"] = MQTTMsgType()


class MQTTTopics(LDict):
    """Topics class."""

    def __init__(
        self, topic_in: str | None = None, topic_out: str | None = None
    ) -> dict:
        super().__init__()

        self["in"] = topic_in
        self["out"] = topic_out


class Command:
    """Landroid Cloud commands."""

    FORCE_REFRESH = 0
    START = 1
    PAUSE = 2
    HOME = 3
    ZONETRAINING = 4
    LOCK = 5
    UNLOCK = 6
    RESTART = 7
    PAUSE_OVER_WIRE = 8
    SAFEHOME = 9


class MQTT(LDict):
    """Full MQTT handler class."""

    def __init__(
        self,
        token: str,
        brandprefix: str,
        endpoint: str,
        user_id: int,
        logger: Logger,
        callback: Any,
    ) -> dict:
        """Initialize AWSIoT MQTT handler."""
        super().__init__()
        # self.client = None
        self._events = EventHandler()
        self._on_update = callback
        self._endpoint = endpoint
        self._log = logger.getChild("MQTT")

        self.connected: bool | None = None

        accesstokenparts = token.replace("_", "/").replace("-", "+").split(".")

        self._uuid = uuid4()

        self.client = mqtt.Client(
            client_id=f"{brandprefix}/USER/{user_id}/bot/{self._uuid}",
            clean_session=False,
            userdata=None,
        )
        self.client.username_pw_set(
            username=f"bot?jwt={urllib.parse.quote(accesstokenparts[0])}.{urllib.parse.quote(accesstokenparts[1])}&x-amz-customauthorizer-name=''&x-amz-customauthorizer-signature={urllib.parse.quote(accesstokenparts[2])}",
            password=None,
        )

        ssl_context = ssl.create_default_context()
        ssl_context.set_alpn_protocols(["mqtt"])
        self.client.tls_set_context(context=ssl_context)

        self.client.on_connect = self._on_connect
        self.client.on_message = self._forward_on_message

    def _forward_on_message(
        self,
        client: mqtt.Client | None,
        userdata: Any | None,
        message: Any | None,
        properties: Any | None = None,  # pylint: disable=unused-argument
    ) -> None:
        """MQTT callback method definition."""
        msg = message.payload.decode("utf-8")
        self._log.debug("Received MQTT message:\n%s", msg)
        self._on_update(msg)

    def subscribe(self, topic: str) -> None:
        """Subscribe to MQTT updates."""
        self.client.subscribe(topic=topic)

    def connect(self) -> None:
        """Connect to the MQTT service."""
        self.client.connect(self._endpoint, 443, 45)
        self.client.loop_start()

    def _on_connect(
        self,
        client: mqtt.Client | None,
        userdata: Any | None,
        flags: Any | None,
        rc: int | None,
        properties: Any | None = None,  # pylint: disable=unused-argument,invalid-name
    ) -> None:
        """MQTT callback method."""
        self._log.debug(connack_string(rc))
        if rc == 0:
            self.connected = True
            self._log.debug("MQTT connected")
        else:
            self.connected = False
            self._log.debug("MQTT connection failed")

    def disconnect(
        self, reasoncode=None, properties=None  # pylint: disable=unused-argument
    ):
        """Disconnect from AWSIoT MQTT server."""
        self.client.disconnect()
        # self._configuration.disconnect()

    def ping(self, serial_number: str, topic: str) -> None:
        """Ping (update) the mower."""
        cmd = self.format_message(serial_number, {"cmd": Command.FORCE_REFRESH})
        self._log.debug("Sending '%s' on topic '%s'", cmd, topic)
        self.client.publish(topic, cmd, 0)
        # self._configuration.publish(topic, cmd, mqtt.QoS.AT_LEAST_ONCE)

    def command(self, serial_number: str, topic: str, action: Command) -> None:
        """Send a specific command to the mower."""
        cmd = self.format_message(serial_number, {"cmd": action})
        self._log.debug("Sending '%s' on topic '%s'", cmd, topic)
        self.client.publish(topic, cmd, 0)
        # self._configuration.publish(topic, cmd, mqtt.QoS.AT_LEAST_ONCE)

    def publish(self, serial_number: str, topic: str, message: dict) -> None:
        """Publish message to the mower."""
        self._log.debug("Publishing message '%s'", message)
        self.client.publish(topic, self.format_message(serial_number, message), 0)
        # self._configuration.publish(
        #     topic,
        #     self.format_message(serial_number, message),
        #     mqtt.QoS.AT_LEAST_ONCE,
        # )

    def format_message(self, serial_number: str, message: dict) -> str:
        """
        Format a message.
        Message is expected to be a dict like this: {"cmd": 1}
        """
        now = datetime.now()
        msg = {
            "id": random.randint(1024, 65535),
            "sn": serial_number,
            "tm": now.strftime("%H:%M:%S"),
            "dt": now.strftime("%d/%m/%Y"),
        }

        msg.update(message)
        self._log.debug("Formatting message '%s' to '%s'", message, msg)

        return json.dumps(msg)
