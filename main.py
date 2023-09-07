import logging
import json
import os

import pyzenbo
from pyzenbo.modules.dialog_system import RobotFace
from pyzenbo.modules.error_code import code_to_description

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.INFO)
host = os.getenv('ZENBO_IP')
sdk = pyzenbo.connect(host)
domain_id = "1303"
domain_uuid = 'E7AABB554ACB414C9AB9BF45E7FA8AD9'
timeout = 15
chat = ChatOpenAI(temperature=0.0)


def on_state_change(serial, cmd, error, state):
    msg = 'on_state_change serial:{}, cmd:{}, error:{}, state:{}'
    print(msg.format(serial, cmd, error, state))
    if error:
        print('on_state_change error:', code_to_description(error))


def listen_callback(args):
    slu_query = args.get('event_slu_query', None)
    if slu_query:
        print(slu_query)


def say_hello_and_ask():
    print('say_hello_and_ask')
    sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
    sdk.robot.jump_to_plan(domain_uuid, 'lanuchHelloWolrd_Plan')
    sdk.robot.speak('Hello, my name is Zenbo Junior. Nice to meet you.')
    slu_result = sdk.robot.wait_for_listen(
        'What task do you want to perform?',
        config={
            'listenLanguageId': 2,
        })
    return slu_result


def execute_command(command):
    template_string = """ \
    You are an Al that controls a smart home. \
    Here is the state of the devices in the home, \
    in JSON format. ```{device_status}``` \
    The user issues the command: {user_command}. \
    Change the device state as appropriate. \
    Provide your response in JSON format.
    """
    user_command = command
    device_status = """ \
    { \
        "user": { \
            "location": "living_room" \
        }, \
        "devices": { \
            "living_room": { \
                "lights": { \
                    "overhead": { \
                        "state": "on" \
                    }, \
                    "lamp": { \
                        "state": "off" \
                    } \
                }, \
                "tvs": { \
                    "living_room_tv": { \
                        "state": "off", \
                        "volume": 0 \
                    } \
                }, \
                "speakers": { \
                    "living_room_speaker": { \
                        "state": "on", \
                        "volume": 0 \
                    } \
                } \
            }, \
            "bedroom": { \
                "lights": { \
                    "bedside_lamp": { \
                        "state": "on" \
                    } \
                } \
            } \
        } \
    }
    """

    prompt_template = ChatPromptTemplate.from_template(template_string)
    status_update_prompt = prompt_template.format_messages(
        user_command=user_command,
        device_status=device_status)

    status_update = chat(status_update_prompt)
    print(status_update.content)


def not_found():
    print('not_found')
    sdk.robot.set_expression(RobotFace.TIRED, timeout=5)
    sdk.robot.speak('No one is here')


sdk.on_state_change_callback = on_state_change
sdk.robot.register_listen_callback(domain_id, listen_callback)
sdk.robot.set_expression(RobotFace.HIDEFACE, timeout=5)

Time = 0

while Time < 5:
    result = sdk.vision.wait_for_detect_face(enable_debug_preview=True,
                                             timeout=timeout)
    print('wait_for_detect_face result:', result)
    if result:
        slu = say_hello_and_ask()
        print('say_hello_and_ask result:', slu)
        json_dict = json.loads(slu['user_utterance'])
        command = json_dict[0]['result'][0]
        execute_command(command)
    else:
        not_found()
    sdk.robot.set_expression(RobotFace.HIDEFACE, timeout=5)
    Time = Time + 1

print("exit")
sdk.robot.stop_speak_and_listen()
sdk.vision.cancel_detect_face()
sdk.release()
