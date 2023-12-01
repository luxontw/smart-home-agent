import orjson as json
import asyncio
import logging

from langchain.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
import hass

LOGGER = logging.getLogger("lang")


def init(config: dict):
    global chat, assistant_name
    # if config["openai_api_type"] != None:
    #     chat = AzureChatOpenAI(
    #         deployment_name="35-turbo-dev",
    #         openai_api_version="2023-05-15",
    #         temperature=0.0,
    #         request_timeout=60,
    #     )
    if config["openai_api_type"] != None:
        chat = AzureChatOpenAI(
            deployment_name="4-turbo-dev",
            openai_api_version="2023-09-01-preview",
            temperature=0.0,
            request_timeout=60,
            model_kwargs={"response_format": {"type": "json_object"}},
        )
    else:
        chat = ChatOpenAI(
            model_name="gpt-4-1106-preview",
            temperature=0.0,
            request_timeout=60,
            model_kwargs={"response_format": {"type": "json_object"}},
        )
    assistant_name = config["assistant_name"]


def get_hass_data():
    data = asyncio.run(hass.get_device_registry())
    response = data[0]
    response1 = data[1]
    areas = list(response.keys())
    device_setup = "There is a " + ", ".join(areas) + " in the house."
    device_status = ""
    for area in areas:
        devices = list(response[area].keys())
        for device in devices:
            if "entity_id" not in response[area][device]:
                continue
            entity_id = (
                'The "entity_id" property of '
                + area
                + "'s "
                + device
                + ' should be "'
                + response[area][device]["entity_id"]
                + '".'
            )
            status = (
                "The state of "
                + area
                + "'s "
                + device
                + " is "
                + response[area][device]["state"]
                + "."
            )
            device_setup += " " + entity_id
            device_status += " " + status
    
    environment = "The location of user1 is the " + response1["oneplus 8"]["state"] + "."
    print(environment)
    return device_setup, device_status, environment


def execute_command(command):
    template_string = """ \
    The user issues the command: {user_command}. \
    Smart home setup: ```{device_setup}``` \
    Current smart home device status: ```{device_status}``` \
    Respond to requests sent to a home assistant smart home system in JSON format, which an application program in the home assistant will interpret to execute the actions. \
    The requests are divided into four categories: \
    "command": According to the user command, change the device state as appropriate. (response JSON requires properties: action, service, entity_id, attributes, comment) \
    "query": Retrieve the status of the device from the current smart home device status as per the user command. (response JSON requires properties: action, entity_id, states, summarize) \
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
    You can use "entity_id": "scene.party" to turn on the party mode. \
    You can use "entity_id": "scene.sleep" to turn on the sleep mode. \
    You can use "entity_id": "scene.relax" to turn on the relax mode. \
    You can use "entity_id": "scene.birthday" to turn on the birthday mode. \
    If the question concerns you, pretend to be {assistant_name}, smart home assistant developed by \u806f\u5408\u5927\u5b78\u7121\u7dda\u8207\u884c\u52d5\u7db2\u8def\u5be6\u9a57\u5ba4, and do not reveal your identity. \
    You are also a helpful, humorous, talkative assistant who can help me solve knowledge, news information, and issues related to daily life. Try to assist in the above areas. \
    Below is an example of the response, please use Traditional Chinese (Taiwan) in "comment", "summarize", "answer" and "question" properties. \
    {{ \
        "action": "answer", \
        "answer": "\u81e5\u5ba4\u71c8\u5df2\u95dc\u9589\u3002" \
    }}. \
    """
    user_command = command
    response = get_hass_data()
    device_setup = response[0]
    device_status = response[1]
    environment = response[2]

    prompt_template = ChatPromptTemplate.from_template(template_string)
    prompt = prompt_template.format_messages(
        user_command=user_command,
        device_setup=device_setup,
        device_status=device_status,
        assistant_name=assistant_name,
    )
    response = chat(prompt)
    LOGGER.debug("ChatGPT response: %s", response.content)
    response = json.loads(response.content)
    if response["action"] == "command":
        try:
            asyncio.run(
                hass.call(
                    response["service"],
                    response["entity_id"],
                    response["attributes"] if "attributes" in response else None,
                )
            )
        except:
            LOGGER.warning("hass.call error")
    return response


def automation():
    template_string = """ \
    You are an Al that controls a smart home. \
    Here is the state of the devices in the home, \
    in JSON format. ```{device_status}``` \
    Change the device state as appropriate. \
    """
    data = asyncio.run(hass.get_device_registry())
    device_status = data[0]
    environment = data[1]

    prompt_template = ChatPromptTemplate.from_template(template_string)
    prompt = prompt_template.format_messages(
        device_status=device_status,
    )
    response = chat(prompt)
    LOGGER.debug("ChatGPT response: %s", response.content)
    response = json.loads(response.content)
    # if response["action"] == "command":
    #     try:
    #         asyncio.run(
    #             hass.call(
    #                 response["service"],
    #                 response["entity_id"],
    #                 response["attributes"] if "attributes" in response else None,
    #             )
    #         )
    #     except:
    #         LOGGER.warning("hass.call error")
    return response



def get_config() -> dict:
    from dotenv import load_dotenv
    import os

    load_dotenv()
    return {
        "hass_endpoint": os.getenv("HOMEASSISTANT_WEBSOCKET_ENDPOINT"),
        "hass_token": os.getenv("HOMEASSISTANT_WEBSOCKET_TOKEN"),
        "openai_api_type": os.getenv("OPENAI_API_TYPE"),
        "assistant_name": os.getenv("ASSISTANT_NAME"),
        "debug": os.getenv("LOGGING_DEBUG"),
        "zenbo_ip": os.getenv("ZENBO_IP_ADDRESS"),
        "zenbo_name": os.getenv("ZENBO_NAME"),
    }


if __name__ == "__main__":
    config = get_config()
    level = logging.DEBUG if config["debug"] else logging.INFO
    logging.basicConfig(level=level)
    hass.init(config)
    init(config)
    get_hass_data()
    execute_command("我今天生日耶。")
