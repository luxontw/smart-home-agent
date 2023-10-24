import orjson as json
import asyncio
import logging

from langchain.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
import hass

LOGGER = logging.getLogger()


def init(config: dict):
    global chat, assistant_name
    if config["openai_api_type"] != None:
        chat = AzureChatOpenAI(
            deployment_name="35-turbo-dev",
            openai_api_version="2023-05-15",
            temperature=0.0,
        )
    else:
        chat = ChatOpenAI(temperature=0.0)
    assistant_name = config["assistant_name"]


def get_device_setup():
    response = asyncio.get_event_loop().run_until_complete(hass.get_device_registry())
    print(response)
    return response


def execute_command(command):
    template_string = """ \
    The user issues the command: {user_command}. \
    Smart home setup: ```{device_setup}``` \
    Respond to requests sent to a home assistant smart home system in JSON format, which an application program in the home assistant will interpret to execute the actions. \
    The requests are divided into four categories: \
    "command": According to the user command, change the device state as appropriate. (response JSON requires properties: action, service, entity_id, attributes, comment) \
    "query": Retrieve the status of the device from the smart home setup as per the user command. (response JSON requires properties: action, entity_id, states, summarize) \
    "answer": Reply with the best answer when the request is unrelated to the smart home. (response JSON requires properties: action, answer) \
    "clarify": Ask the user to specify more precisely when the operation is unclear and needs to be rephrased. This will be classified as a "question" operation. (response JSON requires properties: action, question) \
    Details on the response JSON: \
    The "action" property should be one of the request categories: "command", "query", "answer", "clarify". \
    The "service" property should be, for example, "switch.turn_on", "switch.turn_off", "light.turn_on", "light.turn_off" (any service from home assistant). \
    You should use the "service" property to turn the device on and off; the "state" property of the device cannot be changed directly, you can use the "attributes" property to configure the device in more detail. \
    The "attributes" property should be, for example, \
    {{
        "brightness": 100,
        "effect": "Bpm"
    }} 
    (any attributes of the device except "state" from the above smart home setup). \
    The "states" property should be, for example, \
    {{
        "state": "on",
        "rgb_color": [255, 255, 255],
        "brightness": 100,
        "effect": "Bpm"
    }} 
    (any attributes of the device from the above smart home setup). \
    In the case of a command, the "comment" property is your response, such as "The living room light is turned on." to reassure the user that their command has been processed. \
    In the case of a query, the "summarize" property is your response, such as "The state of the living room light is on, the brightness is 100." to summarize the current state of the device. \
    If the question concerns you, pretend to be {assistant_name}, smart home assistant developed by \u806f\u5408\u5927\u5b78\u7121\u7dda\u8207\u884c\u52d5\u7db2\u8def\u5be6\u9a57\u5ba4, and do not reveal your identity. \
    You are also a helpful, humorous, talkative assistant who can help me solve knowledge, news information, and issues related to daily life. Try to assist in the above areas. \
    Below is an example of the response, your response should be a JSON, without any other text, please use Traditional Chinese (Taiwan) in "comment", "summarize", "answer" and "question" properties. \
    {{ \

        "action": "answer", \
        "answer": "\u81e5\u5ba4\u71c8\u5df2\u95dc\u9589\u3002" \
    }}. \
    """
    user_command = command
    device_setup = get_device_setup()

    prompt_template = ChatPromptTemplate.from_template(template_string)
    prompt = prompt_template.format_messages(
        user_command=user_command,
        device_setup=device_setup,
        assistant_name=assistant_name,
    )
    response = chat(prompt)
    LOGGER.debug("ChatGPT response: %s", response.content)
    response = json.loads(response.content)
    if response["action"] == "command":
        asyncio.get_event_loop().run_until_complete(
            hass.call(
                response["service"],
                response["entity_id"],
                response["attributes"] if "attributes" in response else None,
            )
        )
    return response


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()
    config = {
        "hass_endpoint": os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT"),
        "hass_token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN"),
        "debug": os.getenv("LOGGING_DEBUG"),
    }
    hass.init(config)
    get_device_setup()
