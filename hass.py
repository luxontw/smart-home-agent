import asyncio
import logging
from aiohttp import ClientSession

from hassclient import HomeAssistantClient
from hassclient.models import Event


LOGGER = logging.getLogger()


def init(config: dict) -> None:
    global args
    args = config


async def execute(service, brightness, rgb_color, effect) -> None:
    async with ClientSession() as session:
        await control(session, service, brightness, rgb_color, effect)


async def control(
    session: ClientSession,
    service,
    brightness,
    rgb_color,
    effect,
) -> None:
    """Connect to the server."""
    global args
    websocket_url = args["hass_endpoint"]
    async with HomeAssistantClient(
        websocket_url, args["hass_token"], session
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
