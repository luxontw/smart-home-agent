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


async def start() -> None:
    """Run main."""
    args = get_env()
    level = logging.DEBUG if args["debug"] else logging.INFO
    logging.basicConfig(level=level)

    async with ClientSession() as session:
        await connect(args, session)


async def connect(args: argparse.Namespace, session: ClientSession) -> None:
    """Connect to the server."""
    websocket_url = args["endpoint"]
    async with HomeAssistantClient(websocket_url, args["token"], session) as client:
        await client.subscribe_events(log_events)
        await client.call_service(
            "light",
            "turn_on",
            {"brightness": "100", "rgb_color": ["255", "0", "0"], "effect": "Drip"},
            {"entity_id": "light.wled"},
        )
        await asyncio.sleep(5)


def log_events(event: Event) -> None:
    """Log node value changes."""
    LOGGER.info("Received event: %s", event["event_type"])
    LOGGER.debug(event)


def main() -> None:
    """Run main."""
    with suppress(KeyboardInterrupt):
        asyncio.run(start())

    sys.exit(0)


if __name__ == "__main__":
    main()
