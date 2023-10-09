import json
import asyncio
import logging

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import hass


LOGGER = logging.getLogger()
chat = ChatOpenAI(temperature=0.0)


def get_device_status():
    asyncio.get_event_loop().run_until_complete(
        hass.get_states()
    )


def execute_command(command):
    template_string = """ \
    You are an Al that controls a smart home. \
    Here is the state of the devices in the home, \
    in JSON format. ```{device_status}``` \
    The user issues the command: {user_command}. \
    Change the device state as appropriate. \
    The following are the effects that can be used with led strip: Akemi,Android,Aurora,Black Hole,Blends,Blink,Blink Rainbow,Blobs,Blurz,Bouncing Balls,Bpm,Breathe,Candle,Candle Multi,Chase, \
    choose a suitable one as a led strip effect. \
    Provide your response in JSON format.
    """
    user_command = command

    device_status = """ \
    { \
        "devices": { \
            "living_room": { \
                "lights": { \
                    "led_strip": { \
                        "state": "turn_off" \
                        "brightness": 0 \
                        "rgb_color": [0, 0, 0] \
                        "effect": "Solid" \
                    } \
                } \
            } \
        } \
    }
    """

    prompt_template = ChatPromptTemplate.from_template(template_string)
    status_update_prompt = prompt_template.format_messages(
        user_command=user_command, device_status=device_status
    )

    status_update = chat(status_update_prompt)
    LOGGER.debug("IoT config: %s", status_update.content)
    wled_settings = json.loads(status_update.content)
    service = wled_settings["devices"]["living_room"]["lights"]["led_strip"]["state"]
    brightness = wled_settings["devices"]["living_room"]["lights"]["led_strip"][
        "brightness"
    ]
    rgb_color = wled_settings["devices"]["living_room"]["lights"]["led_strip"][
        "rgb_color"
    ]
    effect = wled_settings["devices"]["living_room"]["lights"]["led_strip"]["effect"]
    asyncio.get_event_loop().run_until_complete(
        hass.call(service, brightness, rgb_color, effect)
    )
