import argparse
import asyncio
import logging
import sys, os
from dotenv import load_dotenv

from contextlib import suppress
from aiohttp import ClientSession

from hassclient import HomeAssistantClient
from hassclient.models import Event

LOGGER = logging.getLogger()


def get_env() -> dict:
    load_dotenv()
    return {
        "endpoint": os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT"),
        "token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN"),
        "debug": os.getenv("HOMEASSISTANT_LOGGING_DEBUG"),
    }

async def execute(service, brightness, rgb_color, effect) -> None:
    args = get_env()
    level = logging.DEBUG if args["debug"] else logging.INFO
    logging.basicConfig(level=level)
    async with ClientSession() as session:
       await control(args, session, service, brightness, rgb_color, effect)


async def control(args: argparse.Namespace, session: ClientSession, service, brightness, rgb_color, effect) -> None:
    """Connect to the server."""
    websocket_url = args["endpoint"]
    async with HomeAssistantClient(websocket_url, args["token"], session) as client:
        if service == "turn_on":
            await client.call_service(
                "light",
                service,
                {"brightness": brightness, "rgb_color": rgb_color, "effect": effect},
                {"entity_id": "light.wled"},
            )
        else:
            await client.call_service(
                "light", service, {"entity_id": "light.wled"}
            )
        await asyncio.sleep(5)
