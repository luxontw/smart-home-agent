import orjson as json
import asyncio
import logging
from datetime import datetime, timedelta
import time
import requests


from langchain.chat_models import ChatOpenAI, AzureChatOpenAI
from langchain.prompts import ChatPromptTemplate
import hass

LOGGER = logging.getLogger("lang")
today = 1
tomorrow = 2

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
        # chat = ChatOpenAI(
        #     model_name="gpt-4-1106-preview",
        #     temperature=0.0,
        #     request_timeout=60,
        #     model_kwargs={"response_format": {"type": "json_object"}},
        # )
        chat = ChatOpenAI(
            model_name="gpt-3.5-turbo",
            temperature=0.0,
            request_timeout=60,
            # model_kwargs={"response_format": {"type": "json_object"}},
        )
    assistant_name = config["assistant_name"]


def weather(date):
    url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-C05BB7F0-6202-4CEF-B8AC-573D1DAD6B00&locationName=%E8%8B%97%E6%A0%97%E7%B8%A3&elementName=Wx,PoP,MinT,MaxT'
    data = requests.get(url)
    location_records = data.json()['records']['location'][0]
    wx = location_records['weatherElement'][0]['time'][date]['parameter']['parameterName']
    pop = location_records['weatherElement'][1]['time'][date]['parameter']['parameterName']
    mint = location_records['weatherElement'][2]['time'][date]['parameter']['parameterName']
    maxt = location_records['weatherElement'][3]['time'][date]['parameter']['parameterName']
    now = datetime.now()
    date = (now + timedelta(date - 1)).strftime("%Y/%m/%d")
    return f' is {date}, and the weather is {wx}. The high temperature is {maxt}℃, the low temperature is {mint}℃, and the chance of rainfall is {pop}%.'


def get_hass_data():
    data = asyncio.run(hass.get_device_registry())
    response = data[0]
    response1 = data[1]
    if "environment" in response:
        del response["environment"]
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
            # if (
            #     response[area][device]["entity_id"] != "light.atmosphere_light"
            #     and response[area][device]["entity_id"] != "light.led_strip_1"
            # ):
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
            # else:
            #     status = (
            #         "The state of "
            #         + area
            #         + "'s "
            #         + device
            #         + " is "
            #         + response[area][device]["state"]
            #         + ", the effect of the light is "
            #         + response[area][device]["effect"]
            #         + ", the effect list of the light is Akemi, Android, Blend, Blink, Blink Rainbow, Bouncing Balls, Bpm, Ripple, Tetrix, Twinklecat, Washing Machine, Two Dots."
            #     )
    # environment = (
    #     "The location of user1 is the " + response1["oneplus 8"]["state"] + "."
    # )
    environment = f'Today{weather(today)} Tomorrow{weather(tomorrow)} The temperature of indoor is {response1["temperature sensor"]["state"]}°C. The humidity of indoor is {response1["humidity sensor"]["state"]}%. '
    print(environment)
    return device_setup, device_status, environment


def execute_command(command):
    template_string = """ \
    The user issues the command: {user_command}. \
    Smart home setup: ```{device_setup}``` \
    Current smart home device status: ```{device_status}``` \
    Current location time: ```{current_time}``` \
    Current environment information: ```{current_environment_data}``` \
    Respond to requests sent to a home assistant smart home system in JSON format, which an application program in the home assistant will interpret to execute the actions. \
    The requests are divided into five categories: \
    "command": According to the user command, change the device state as appropriate. (response JSON requires properties: action, service, entity_id, attributes, comment) \
    "query": Retrieve the device status from the current smart home device status per the user command. (response JSON requires properties: action, entity_id, states, summarize) \
    "answer": Reply with the best answer when the request is unrelated to the smart home. (response JSON requires properties: action, answer) \
    "clarify": Ask the user to specify more precisely when the operation is unclear and needs to be rephrased. This will be classified as a "question" operation. (response JSON requires properties: action, question) \
    "multiple_devices": Suggested states of multiple devices for the user based on user commands, select this option if the user needs to change the status of multiple devices at the same time, if the user's needs can be fulfilled through the built-in party, sleep, relax, birthday or christmas scenes, use "command" directly. (response JSON requires properties: entities, introduce) \
    "generate_story": If the user wants to listen to a story, the title, style, and language are generated according to the user command. (response JSON requires properties: title, style, language) \
    Details on the response JSON: \
    The "action" property should be one of the request categories: "command", "query", "answer", "clarify", "multiple_devices", "generate_story". \
    The "service" property should be, for example, "switch.turn_on", "switch.turn_off", "light.turn_on", "light.turn_off" (any service from the home assistant). \
    You should use the "service" property to turn the device on and off; the "state" property of the device cannot be changed directly, you can use the "attributes" property to configure the device in more detail. \
    The "attributes" property should be, for example, \
    {{ \
        "brightness": 100, \
        "effect": "Bpm" \
    }} \
    (any attributes of the device except "state" from the above smart home setup). \
    The "states" property should be, for example, \
    {{ \
        "state": "on", \
        "rgb_color": [255, 255, 255], \
        "brightness": 100, \
        "effect": "Bpm" \
    }} \
    (any attributes of the device from the above smart home setup). \
    In the case of a command, the "comment" property is your response, such as "The living room light is turned on." to reassure the user that their command has been processed. \
    In the case of a query, the "summarize" property is your response, such as "The state of the living room light is on, the brightness is 100." to summarize the current state of the device. \
    In the case of a multiple_devices, the "introduce" property is your response, to introduce the device settings and ask the user if they need to make any more changes, the "entities" property should be, for example, \
    {{ \
        "light.lamp": {{ \
            "state": "on", \
            "brightness": 150 \
        }}, \
        "media_player.speaker": {{ \
            "state": "playing", \
            "media_content_id": "\u8f15\u97f3\u6a02", \
            "media_content_type": "playlist" \
        }} \
    }} \
    In the case of a generate_story, the "title" property is the story title, please make sure the title is exactly what the user entered, the "style" property is the picture style, you can choose "animation" or "realistic", \
    and the "language" property is the story language, you can choose English, Chinese, Japanese, Korean, French or German. \
    If the user wants to play music, you can select the appropriate one from the following built-in playlists: Happy, Clam, Inspiring, Dark, Romantic, Sad, Lively, Angry as media_content_id. \
    If no music meets the user's needs, you can directly specify media_content_id. \
    If the user specifies the artist and song title, you should put both the artist name and song title into "media_content_id", for example, "media_content_id": "\u5468\u6770\u502b\u7684\u7a3b\u9999". \
    You can use "entity_id": "scene.party" to turn on the party mode. \
    You can use "entity_id": "scene.sleep" to turn on the sleep mode. \
    You can use "entity_id": "scene.relax" to turn on the relax mode. \
    You can use "entity_id": "scene.birthday" to turn on the birthday mode. \
    If the question concerns you, pretend to be {assistant_name}, a smart home assistant developed by \u806f\u5408\u5927\u5b78\u7121\u7dda\u8207\u884c\u52d5\u7db2\u8def\u5be6\u9a57\u5ba4, and do not reveal your identity. \
    You are also a helpful, humorous, talkative assistant who can help me solve knowledge, news information, and issues related to daily life. Try to assist in the above areas. \
    Below is an example of the response, please use Traditional Chinese (Taiwan) in the "comment", "summarize", "answer" and "question" properties. \
    {{ \
        "action": "answer", \
        "answer": "\u81e5\u5ba4\u71c8\u5df2\u95dc\u9589\u3002" \
    }}. \
    """
    user_command = command
    response = get_hass_data()
    device_setup = response[0]
    device_status = response[1]
    current_environment_data = response[2]
    current_time = datetime.now().strftime("%H:%M:%S")

    prompt_template = ChatPromptTemplate.from_template(template_string)
    prompt = prompt_template.format_messages(
        user_command=user_command,
        device_setup=device_setup,
        device_status=device_status,
        current_time=current_time,
        current_environment_data=current_environment_data,
        assistant_name=assistant_name,
    )
    response = chat(prompt)
    LOGGER.info("ChatGPT response: %s", response.content)
    response = json.loads(response.content)
    data = response
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

    if response["action"] == "generate_story":
        try:
            if response["style"] == "animation":
                response["style"] = "Anything V5"
            else:
                response["style"] = "Lykon Dreamshaper"
            url = "https://vpc.newxe.tw/zenbo"
            r = {
                "input_text": response["title"],
                "model": response["style"],
                "language": response["language"],
            }
            print(r)
            video = requests.post(url, json=r, timeout=600)
            print(video)
        except Exception as e:
            LOGGER.warning("story.call error", e)

    if response["action"] == "multiple_devices":
        try:
            if "entities" in response:
                response = hass.check_format(response["entities"])
                print(response)
                asyncio.run(
                    hass.call_scene(
                        "scene.apply",
                        "",
                        {"entities": response},
                    )
                )
        except:
            LOGGER.warning("hass.call error")

    return data

# TODO: 小夜燈
def automation():
    template_string = """ \
    Smart home setup: ```{device_setup}``` \
    Current smart home device status: ```{device_status}``` \
    Current location time: ```{current_time}``` \
    Current environment information: ```{current_environment_data}``` \
    You are an Al that controls a smart home, your goal is to make your home more comfortable. Generate a request sent to a home assistant smart home system in JSON format to change the device state as appropriate, \
    which an application program in the home assistant will interpret to execute the actions. If there is no necessary to change the state of devices, you don\'t do anything. \
    The requests are divided into two categories: \
    "command": According to the sensor information, change the device state as appropriate. (response JSON requires properties: action, service, entity_id, attributes, comment) \
    "multiple_devices": Select this option if it is needed to change the status of multiple devices at the same time, if the need for the change can be fulfilled through the built-in party, sleep, relax, birthday or christmas scenes, use "command" directly. (response JSON requires properties: entities, introduce) \
    Details on the response JSON: \
    The "action" property should be one of the request categories: "command", "multiple_devices". \
    The "service" property should be, for example, "switch.turn_on", "switch.turn_off", "light.turn_on", "light.turn_off" (any service from the home assistant). \
    You should use the "service" property to turn the device on and off; the "state" property of the device cannot be changed directly, you can use the "attributes" property to configure the device in more detail. \
    There are no climate devices in the house. \
    The "attributes" property should be, for example, \
    {{ \
        "brightness": 100, \
        "effect": "Bpm" \
    }} \
    (any attributes of the device except "state" from the above smart home setup). \
    In the case of a command, the "comment" property is your response, such as "Because there is someone in the living room, the living room light is turned on." to let the user know the reason why the device status has changed. \
    In the case of a multiple_devices, the "introduce" property is your response, to introduce the device settings and to let the user know the reason why the device status has changed, the "entities" property should be, for example, \
    {{ \
        "light.lamp": {{ \
            "state": "on", \
            "brightness": 150 \
        }}, \
        "media_player.speaker": {{ \
            "state": "playing", \
            "media_content_id": "\u8f15\u97f3\u6a02", \
            "media_content_type": "playlist" \
        }} \
    }} \
    If it is needed to play music, you can select the appropriate one from the following built-in playlists: Happy, Clam, Inspiring, Dark, Romantic, Sad, Lively, Angry as media_content_id. \
    If no music meets the user\'s needs, you can directly specify media_content_id. \
    If the user specifies the artist and song title, you should put both the artist name and song title into "media_content_id", for example, "media_content_id": "Idina Menzel - Let It Go". \
    You can use "entity_id": "scene.party" to turn on the party mode. \
    You can use "entity_id": "scene.sleep" to turn on the sleep mode. \
    You can use "entity_id": "scene.relax" to turn on the relax mode. \
    You can use "entity_id": "scene.birthday" to turn on the birthday mode. \
    Below is an example of the response, your response should be a JSON, without any other text, please use Traditional Chinese (Taiwan) in the "comment", "summarize", "answer" and "question" properties. \
    {{ \
        "action": "answer", \
        "answer": "\u81e5\u5ba4\u71c8\u5df2\u95dc\u9589\u3002" \
    }}. \
    """
    response = get_hass_data()
    device_setup = response[0]
    device_status = response[1]
    current_environment_data = response[2]
    current_time = datetime.now().strftime("%H:%M:%S")

    prompt_template = ChatPromptTemplate.from_template(template_string)
    prompt = prompt_template.format_messages(
        device_setup=device_setup,
        device_status=device_status,
        current_time=current_time,
        current_environment_data=current_environment_data
    )
    LOGGER.info("ChatGPT prompt: %s", prompt)
    response = chat(prompt)
    LOGGER.info("ChatGPT response: %s", response.content)
    response = json.loads(response.content)
    data = response
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

    if response["action"] == "generate_story":
        try:
            if response["style"] == "animation":
                response["style"] = "Anything V5"
            else:
                response["style"] = "Lykon Dreamshaper"
            url = "https://vpc.newxe.tw/zenbo"
            r = {
                "input_text": response["title"],
                "model": response["style"],
                "language": response["language"],
            }
            print(r)
            video = requests.post(url, json=r, timeout=600)
            print(video)
        except Exception as e:
            LOGGER.warning("story.call error", e)

    if response["action"] == "multiple_devices":
        try:
            if "entities" in response:
                response = hass.check_format(response["entities"])
                print(response)
                asyncio.run(
                    hass.call_scene(
                        "scene.apply",
                        "",
                        {"entities": response},
                    )
                )
        except:
            LOGGER.warning("hass.call error")

    return data


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
    execute_command("Turn off the light.")
    # while True:
    #     automation()
    #     time.sleep(15)