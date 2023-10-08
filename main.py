import os
import logging
from contextlib import suppress
from dotenv import load_dotenv

import zenbo
import hass


def get_config() -> dict:
    load_dotenv()
    return {
        "hass_endpoint": os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT"),
        "hass_token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN"),
        "debug": os.getenv("LOGGING_DEBUG"),
        "zenbo_ip": os.getenv("ZENBO_IP_ADDRESS"),
        "zenbo_name": os.getenv("ZENBO_NAME"),
    }


if __name__ == "__main__":
    config = get_config()
    level = logging.DEBUG if config["debug"] else logging.INFO
    logging.basicConfig(level=level)
    with suppress(KeyboardInterrupt):
        hass.init(config)
        zenbo.init(config)
