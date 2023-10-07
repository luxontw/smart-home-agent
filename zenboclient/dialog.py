"""
Voice recognition and dialog related functions to interact between Zenbo
and the user.
"""
import pyzenbo
import json
import llm
import hass
import asyncio
from pyzenbo.modules.dialog_system import RobotFace

global name, been_called
name = "助理"
been_called = False


def handle_speak(zenbo: pyzenbo.PyZenbo, args):
    """
    Handles user speaking -- whenever user says something, Zenbo calls this function.
    """
    event_user_utterance = args.get("event_user_utterance", None)

    if event_user_utterance:
        global been_called
        print("event_user_utterance: ", event_user_utterance)
        been_said = str(
            json.loads(event_user_utterance.get("user_utterance"))[0].get("result")[0]
        )
        print("been_said: ", been_said)

        if been_said == name:
            welcome(zenbo)
        elif been_called:
            if been_said == "不用了":
                pass
            else:
                print("control: ", been_said)
                result = llm.execute_command(been_said)
                wled_settings = json.loads(result)
                service = wled_settings["devices"]["living_room"]["lights"]["led_strip"]["state"]
                brightness = wled_settings["devices"]["living_room"]["lights"]["led_strip"][
                    "brightness"
                 ]
                rgb_color = wled_settings["devices"]["living_room"]["lights"]["led_strip"][
                  "rgb_color"
                ]
                effect = wled_settings["devices"]["living_room"]["lights"]["led_strip"][
                    "effect"
                ]
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                asyncio.get_event_loop().run_until_complete(hass.execute(service, brightness, rgb_color, effect))
                been_called = False


def wait_user(zenbo: pyzenbo.PyZenbo):
    """
    Wait the user speak something.
    """
    print("wait_user")
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    slu_result = zenbo.robot.wait_for_listen(
        "",
        config={
            "listenLanguageId": 1,
        },
    )
    return slu_result


def welcome(zenbo: pyzenbo.PyZenbo):
    """
    Asks the user if he/she wants to do something.
    """
    print("welcome")
    global been_called
    been_called = True
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    zenbo.robot.speak("你好我是" + name + "，很高興認識你。")
    slu_result = zenbo.robot.wait_for_listen(
        "需要什麼協助嗎?",
        config={
            "listenLanguageId": 1,
        },
    )
    return slu_result


def say_fine(zenbo: pyzenbo.PyZenbo):
    """
    FFFFINE.
    """
    zenbo.robot.speak("Fine.")
