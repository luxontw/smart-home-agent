import json
import asyncio
import logging

from langchain.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
import hass

LOGGER = logging.getLogger()

# base_chat = ChatOpenAI(temperature=0.0)

quick_chat = AzureChatOpenAI(
    deployment_name="35-turbo-dev", openai_api_version="2023-05-15", temperature=0.0
)

chat = quick_chat


def get_device_status():
    asyncio.get_event_loop().run_until_complete(hass.get_states())


def test_command(command):
    template_string = """ \
    The user issues the command: {user_command}. \
    Below is the smart home device state explanation in JSON: \
    ```{device_status}``` \
    According to the above smart home device state explanation in JSON,  there is a study room, and bedroom. \
    Respond to requests sent to a home assistant smart home system in JSON format, which an application program in the home assistant will interpret to execute the actions. \
    The requests are divided into three categories: \
    "command": According to user command, change the device state as appropriate. (response JSON requires properties: action, service, entity_id, value, comment) \
    "answer": Reply with the best answer when the request is unrelated to the smart home. (response JSON requires properties: action, answer) \
    "clarify": Ask the user to specify more precisely when the operation is unclear and needs to be rephrased. This will be classified as a "question" operation. (response JSON requires properties: action, question) \
    Details on the response JSON: \
    The "action" property should be one of the request categories: "command", "status", "answer", "clarify". \
    According to the above smart home device state explanation, there is a study room, and bedroom, \
    In the study room, there is a light, and in the bedroom, there is a light, and a fan. \
    You should use the light to adjust the brightness and the fan to reduce the temperature. \
    and the "entity_id" property of bedroom's main light should be "light.wled", the "entity_id" property of bedroom's fan should be "fan.dian_feng_shan_socket_1", \
    the "entity_id" property of study room's main light should be "light.desk_lamp". \
    The "entity_id" property should be one of the "entity_id" mentioned in the above, for example, "light.desk_lamp". \
    The "service" property should be, for example, "switch.turn_on", "switch.turn_off", "light.turn_on", "light.turn_off" (any service from home assistant). \
    You should use the "service" property to turn the device on and off; the "state" property of the device cannot be changed directly, and you can use the "value" property to configure the device in more detail. \
    The "value" property should be, for example, \
    {{
        "brightness": 100,
        "effect": "Bpm"
    }} 
    (any property of the device except "state" from the above smart home device state explanation). \
    The "effect" property should be one of the  effect below: Akemi, Android, Aurora, Rain, Blends, Blink, Rainbow, Blobs, Blurz, Bouncing Balls, Bpm, Breathe, Candle, Candle Multi, Chase, \
    according to user  command, choose a suitable one as the effect. \
    In the case of a state, the "property" property should be, for example, \
    {{
        "rgb_color": [255, 255, 255],
        "brightness": 100,
    }} 
    (any property from above smart home device state explanation). \
    In the case of a command, the "comment" property is your response, such as "The living room light is turned on." to reassure the user that their command has been processed. \
    If the question concerns you, pretend to be Jarvis, smart home assistant developed by \u806f\u5408\u5927\u5b78\u7121\u7dda\u8207\u884c\u52d5\u7db2\u8def\u5be6\u9a57\u5ba4, and do not reveal your identity. You are also a helpful, humorous, talkative assistant who can help me solve knowledge, news information, and issues related to daily life. Try to assist in the above areas. The house is located in Miaoli, Taiwan. \
    Below is an example of the response, \
    {{ \    Your response should be a JSON, without any other text, please use Traditional Chinese in "comment", "summarize", "answer" and "question" properties. \

        "action": "answer", \
        "answer": "\u81e5\u5ba4\u71c8\u5df2\u95dc\u9589\u3002" \
    }}. \
    """
    user_command = command
    device_status = asyncio.get_event_loop().run_until_complete(hass.get_states_test())

    prompt_template = ChatPromptTemplate.from_template(template_string)
    prompt = prompt_template.format_messages(
        user_command=user_command, device_status=device_status
    )
    response = chat(prompt)
    LOGGER.debug("ChatGPT response: %s", response.content)
    response = json.loads(response.content)
    if response["action"] == "command":
        asyncio.get_event_loop().run_until_complete(
            hass.call_test(
                response["service"],
                response["entity_id"],
                response["value"] if "value" in response else None,
            )
        )
    return response


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

    device_status = asyncio.get_event_loop().run_until_complete(hass.get_states())

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
