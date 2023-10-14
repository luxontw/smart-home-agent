import asyncio
import logging
import json
from aiohttp import ClientSession

from hassclient import HomeAssistantClient
from hassclient.models import Event, State


LOGGER = logging.getLogger()


def init(config: dict) -> None:
    global args, session
    args = config
    session = ClientSession()


async def get_states() -> State:
    """Connect to the server."""
    global args, session
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        states = await client.get_states()
        for state in states:
            if state["entity_id"] == "light.wled":
                LOGGER.debug("Received state: %s", state)
                device_status = f""" \
                {{ \
                    "devices": {{ \
                        "living_room": {{ \
                            "lights": {{ \
                                "led_strip": {{ \
                                    "state": "turn_{state["state"]}" \
                                    "brightness": {0 if state["state"] == "off" else state["attributes"]["brightness"]} \
                                    "rgb_color": {[0, 0, 0] if state["state"] == "off" else state["attributes"]["rgb_color"]}  \
                                    "effect": "{"none" if state["state"] == "off" else state["attributes"]["effect"]}"  \
                                }} \
                            }} \
                        }} \
                    }} \
                }}
                """
                LOGGER.debug("Sending device status: %s", device_status)
                return device_status


async def get_states_test() -> State:
    """Connect to the server."""
    global args, session, device_status
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        states = await client.get_states()
        device_status = f"""
        {{ \
            "devices": {{ \
                "fans": {{ \
        """
        for state in states:
            if state["entity_id"] == "fan.dian_feng_shan_socket_1":
                device_status += f""" \
                    "{state["attributes"]["friendly_name"]}": {{ \
                        "entity_id": "{state["entity_id"]}", \
                        "state": "{state["state"]}", \
                        "area"  : "bedroom" \
                    }} \
                 }}, \
                """
            if state["entity_id"] == "light.wled":
                device_status += f""" \
                    "{state["attributes"]["friendly_name"]}": {{ \
                        "entity_id": "{state["entity_id"]}", \
                        "state": "{state["state"]}", \
                        "brightness": {0 if state["state"] == "off" else state["attributes"]["brightness"]} ,\
                        "rgb_color": {[0, 0, 0] if state["state"] == "off" else state["attributes"]["rgb_color"]}  ,\
                        "effect": "{"none" if state["state"] == "off" else state["attributes"]["effect"]}"  ,\
                        "area"  : "bedroom" \
                    }} \
                }} \
                """
            if state["entity_id"] == "light.desk_lamp":
                device_status += f""" \
                "lights": {{ \
                    "{state["attributes"]["friendly_name"]}": {{ \
                        "entity_id": "{state["entity_id"]}", \
                        "state": "{state["state"]}" ,\
                        "brightness": {0 if state["state"] == "off" else state["attributes"]["brightness"]} ,\
                        "color_temp_kelvin": {0 if state["state"] == "off" else state["attributes"]["color_temp_kelvin"]}, \
                        "area"  : "study_room" \
                    }}, \
                """
            # LOGGER.debug("Received state: %s", state)
    device_status += f""" \
        }} \
    }} \
    """
    LOGGER.debug("Sending device status: %s", device_status)
    return device_status


async def call_test(
    service,
    entity_id,
    value,
) -> None:
    """Connect to the server."""
    global args, session
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        if entity_id == "light.desk_lamp" and value:
            if "brightness" in value:
                value["brightness"] = float(int(value["brightness"]) * 255 / 100)
        if service == "fan.turn_on":
            await client.call_service(
                "fan",
                "turn_on",
                value,
                {"entity_id": entity_id},
            )
        elif service == "fan.turn_off":
            await client.call_service("fan", "turn_off", {"entity_id": entity_id})
        if service == "light.turn_on":
            await client.call_service(
                "light",
                "turn_on",
                value,
                {"entity_id": entity_id},
            )
        elif service == "light.turn_off":
            await client.call_service("light", "turn_off", {"entity_id": entity_id})
        await asyncio.sleep(5)


async def call(
    service,
    brightness,
    rgb_color,
    effect,
) -> None:
    """Connect to the server."""
    global args, session
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        if service == "turn_on":
            await client.call_service(
                "light",
                service,
                {"brightness": brightness, "rgb_color": rgb_color, "effect": effect},
                {"entity_id": "light.wled"},
            )
        else:
            await client.call_service("light", service, {"entity_id": "light.wled"})
        await asyncio.sleep(5)


def log_events(event: Event) -> None:
    """Log node value changes."""
    LOGGER.info("Received event: %s", event["event_type"])
    LOGGER.debug(event)


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    from contextlib import suppress

    load_dotenv()
    config = {
        "hass_endpoint": os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT"),
        "hass_token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN"),
        "debug": os.getenv("LOGGING_DEBUG"),
        "zenbo_ip": os.getenv("ZENBO_IP_ADDRESS"),
        "zenbo_name": os.getenv("ZENBO_NAME"),
    }
    level = logging.DEBUG if config["debug"] else logging.INFO
    logging.basicConfig(level=level)
    with suppress(KeyboardInterrupt):
        init(config)
        asyncio.get_event_loop().run_until_complete(get_states_test())
