"""
Voice recognition and dialog related functions to interact between Zenbo
and the user.
"""
import pyzenbo
import json
import logging
import lang
import zenboclient.navigation as navigation

from pyzenbo.modules.dialog_system import RobotFace

LOGGER = logging.getLogger("zenboclient.dialog")
been_called = False
keep_chat = False


def welcome(zenbo: pyzenbo.PyZenbo, name: str, been_called: bool = False):
    """
    Asks the user if he/she wants to do something.
    """
    LOGGER.info("func: %s", "welcome")
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    if been_called:
        zenbo.robot.speak("你好")
    else:
        zenbo.robot.speak("你好我是" + name + "，很高興認識你。需要什麼協助嗎?")


def reply_user_command(zenbo: pyzenbo.PyZenbo, command: str):
    """
    Reply to the user command.
    """
    LOGGER.info("func: %s", "reply_user_command")
    global keep_chat
    zenbo.robot.set_expression(RobotFace.AWARE_RIGHT, timeout=5)
    response = lang.execute_command(command)
    zenbo.robot.set_expression(RobotFace.CONFIDENT_ADV, timeout=5)
    if response["action"] == "command":
        reply = response["comment"]
        keep_chat = False
        if response["entity_id"] == "scene.party":
            navigation.dance(zenbo, reply)
            reply = ""
        if response["entity_id"] == "scene.sleep":
            navigation.sleep(zenbo)
    elif response["action"] == "query":
        reply = response["summarize"]
        keep_chat = False
    elif response["action"] == "answer":
        reply = response["answer"]
        keep_chat = False
    elif response["action"] == "clarify":
        reply = response["question"]
        keep_chat = True
    else:
        reply = "抱歉，我不太明白。"
    zenbo.robot.speak(reply)
