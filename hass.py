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


async def get_all_states() -> dict:
    """Connect to the server."""
    global args, session
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        states = await client.get_states()
        LOGGER.debug("Received states: %s", states)
        return states


async def get_device_registry() -> json:
    """Connect to the server."""
    global args, session
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        device_registry = await client.get_device_registry()
        response = {}
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
        response = json.dumps(response)
        LOGGER.debug("Received device registry: %s", response)
        return response


async def call(
    service,
    entity_id,
    attributes,
) -> None:
    """Connect to the server."""
    global args, session
    async with HomeAssistantClient(
        args["hass_endpoint"], args["hass_token"], session
    ) as client:
        # if entity_id == "light.desk_lamp" and attributes:
        #     if "brightness" in attributes:
        #         attributes["brightness"] = float(
        #             int(attributes["brightness"]) * 255 / 100
        #         )
        domain, service = service.split(".")
        await client.call_service(
            domain,
            service,
            attributes,
            {"entity_id": entity_id},
        )


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
        asyncio.get_event_loop().run_until_complete(get_device_registry())
