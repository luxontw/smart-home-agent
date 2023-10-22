"""
Voice recognition and dialog related functions to interact between Zenbo
and the user.
"""
import pyzenbo
import json
import logging

from pyzenbo.modules.dialog_system import RobotFace

LOGGER = logging.getLogger()


def handle_speak(zenbo: pyzenbo.PyZenbo, args):
    """
    Handles user speaking -- whenever user says something, Zenbo calls this function.
    """
    LOGGER.info("handle_speak")
    event_user_utterance = args.get("event_user_utterance", None)

    if event_user_utterance:
        LOGGER.debug("event_user_utterance:  %s", event_user_utterance)
        been_said = str(
            json.loads(event_user_utterance.get("user_utterance"))[0].get("result")[0]
        )
        LOGGER.info("been_said : %s", been_said)


def wait_user_speak(zenbo: pyzenbo.PyZenbo):
    """
    Wait the user speak something.
    """
    LOGGER.info("been_said : %s", "wait_user")
    zenbo.robot.set_expression(RobotFace.DEFAULT, timeout=5)
    slu_result = zenbo.robot.wait_for_listen(
        "",
        config={
            "listenLanguageId": 1,
        },
    )
    return slu_result


def welcome(zenbo: pyzenbo.PyZenbo, name: str, been_called: bool = False):
    """
    Asks the user if he/she wants to do something.
    """
    LOGGER.info("been_said : %s", "welcome")
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    if been_called:
        slu_result = zenbo.robot.wait_for_listen(
            "你好",
            config={
                "listenLanguageId": 1,
            },
        )
        zenbo.robot.set_expression(RobotFace.AWARE_RIGHT, timeout=5)
    else:
        zenbo.robot.speak("你好我是" + name + "，很高興認識你。")
        slu_result = zenbo.robot.wait_for_listen(
            "需要什麼協助嗎?",
            config={
                "listenLanguageId": 1,
            },
        )
        zenbo.robot.set_expression(RobotFace.AWARE_RIGHT, timeout=5)
    return slu_result
