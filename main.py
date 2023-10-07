from contextlib import suppress

import zenbo
import llm
import hass


if __name__ == "__main__":
    with suppress(KeyboardInterrupt):
        zenbo.init()
        hass.init()
