import asyncio
import logging
import orjson as json
from aiohttp import ClientSession

from hassclient import HomeAssistantClient
from hassclient.models import Event, State


LOGGER = logging.getLogger("hass")


def init(config: dict) -> None:
    global args
    args = config


async def get_device_registry() -> dict:
    """Connect to the server."""
    session = ClientSession()
    response = {}
    environment = {}
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        device_registry = await client.get_device_registry()
        cache = {}
        for device in device_registry:
            if device["area_id"] != None and device["name_by_user"] != None:
                area = device["area_id"]
                name = device["name_by_user"]
                if area not in response:
                    response[area] = {}
                    response[area][name] = {}
                else:
                    response[area][name] = {}
                cache[name] = area

        states = await client.get_states()
        for state in states:
            str = state["entity_id"]
            name = str[str.rfind(".") + 1 :].replace("_", " ")
            if name in cache:
                response[cache[name]][name] = state["attributes"]
                response[cache[name]][name]["entity_id"] = state["entity_id"]
                response[cache[name]][name]["state"] = state["state"]
            # TODO: Avoid specifying the entity_id directly
            elif state["entity_id"] == "sensor.oneplus_8":
                environment["oneplus 8"] = state["attributes"]
                environment["oneplus 8"]["entity_id"] = state["entity_id"]
                environment["oneplus 8"]["state"] = state["state"]
            elif state["entity_id"] == "sensor.humidity_sensor":
                environment["humidity sensor"] = state["attributes"]
                environment["humidity sensor"]["entity_id"] = state["entity_id"]
                environment["humidity sensor"]["state"] = state["state"]
            elif state["entity_id"] == "sensor.temperature_sensor":
                environment["temperature sensor"] = state["attributes"]
                environment["temperature sensor"]["entity_id"] = state["entity_id"]
                environment["temperature sensor"]["state"] = state["state"]
            elif state["entity_id"] == "sensor.temperature_sensor":
                environment["temperature sensor"] = state["attributes"]
                environment["temperature sensor"]["entity_id"] = state["entity_id"]
                environment["temperature sensor"]["state"] = state["state"]
            elif state["entity_id"] == "camera.cam1":
                environment["indoor camera"] = {}
                environment["indoor camera"]["entity_id"] = state["entity_id"]
                environment["indoor camera"][
                    "image"
                ] = f'https://ha.newxe.tw{state["attributes"]["entity_picture"]}'

    await session.close()
    return response, environment


def check_format(entities: dict) -> dict:
    for entity_id, attributes in entities.items():
        print(entity_id, attributes)
        if attributes and entity_id == "light.lamp":
            if "brightness" in attributes:
                brightness = int(attributes["brightness"])
                if brightness > 100:
                    brightness = float(brightness / 255) * 255
                else:
                    brightness = float(brightness / 100) * 255
                attributes["brightness"] = round(brightness, 0)
        if attributes and entity_id == "media_player.speaker":
            if (
                "media_content_id" in attributes
                or "media_content_type" in attributes
                or attributes["state"] == "on"
            ):
                attributes["media_content_type"] = "playlist"
                attributes["state"] = "playing"
        if (
            attributes
            and entity_id == "light.led_strip_1"
            or entity_id == "light.led_strip"
        ):
            if "effect" in attributes:
                if attributes["effect"] == "party" or attributes["effect"] == "Party":
                    attributes["effect"] = "Colortwinkles"
                if attributes["effect"] == "movie" or attributes["effect"] == "Movie":
                    attributes["effect"] = "Theater"
                if attributes["effect"] == "cinema" or attributes["effect"] == "Cinema":
                    attributes["effect"] = "Theater"
                if attributes["effect"] == "music" or attributes["effect"] == "Music":
                    attributes["effect"] = "Wavesins"
                if attributes["effect"] == "music" or attributes["effect"] == "Music":
                    attributes["effect"] = "Wavesins"
                if attributes["effect"] == "relax" or attributes["effect"] == "Relax":
                    attributes["effect"] = "Breathe"
    return entities


async def call_scene(
    service,
    entity_id,
    attributes,
) -> None:
    """Connect to the server."""
    session = ClientSession()
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        domain, service = service.split(".")
        await client.call_service(
            domain,
            service,
            attributes,
            {},
        )
    await session.close()


async def call(
    service,
    entity_id,
    attributes,
) -> None:
    """Connect to the server."""
    session = ClientSession()
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        if attributes and entity_id == "fan.stand_fan":
            attributes = []
        if attributes and entity_id == "light.lamp":
            if "brightness" in attributes:
                brightness = int(attributes["brightness"])
                if brightness > 100:
                    brightness = float(brightness / 255) * 255
                else:
                    brightness = float(brightness / 100) * 255
                attributes["brightness"] = round(brightness, 0)
        if attributes and entity_id == "media_player.speaker":
            if "media_content_type" in attributes:
                if attributes["media_content_type"] == "music":
                    attributes["media_content_type"] = "playlist"
        if attributes and "scene" in entity_id:
            attributes = []
        if (
            attributes
            and entity_id == "light.led_strip_1"
            or entity_id == "light.led_strip"
        ):
            if service == "turn_off":
                attributes = []
            if "effect" in attributes:
                if attributes["effect"] == "party" or attributes["effect"] == "Party":
                    attributes["effect"] = (
                        "colortwinkles" or attributes["effect"] == "Colortwinkles"
                    )
                if attributes["effect"] == "movie" or attributes["effect"] == "Movie":
                    attributes["effect"] = "Theater"
                if attributes["effect"] == "cinema" or attributes["effect"] == "Cinema":
                    attributes["effect"] = "Theater"
                if attributes["effect"] == "music" or attributes["effect"] == "Music":
                    attributes["effect"] = "Wavesins"
                if attributes["effect"] == "music" or attributes["effect"] == "Music":
                    attributes["effect"] = "Wavesins"
                if attributes["effect"] == "relax" or attributes["effect"] == "Relax":
                    attributes["effect"] = "Breathe"
        if "state" in attributes:
            del attributes["state"]
        domain, service = service.split(".")
        await client.call_service(
            domain,
            service,
            attributes,
            {"entity_id": entity_id},
        )
    await session.close()


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
        result = asyncio.run(get_device_registry())
        print(result)
