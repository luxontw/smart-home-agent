import asyncio
import logging
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
        state = await client.get_states()
        return state


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
