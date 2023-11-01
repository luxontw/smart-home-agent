"""
Voice recognition and dialog related functions to interact between Zenbo
and the user.
"""
import pyzenbo
import json
import logging
import lang

from pyzenbo.modules.dialog_system import RobotFace

LOGGER = logging.getLogger("zenboclient.dialog")
been_called = False
keep_chat = False


def listen_callback_handler(zenbo: pyzenbo.PyZenbo, args):
    pass


def wait_user_speak(zenbo: pyzenbo.PyZenbo, config: dict):
    """
    Wait the user speak something.
    """
    LOGGER.info("func: %s", "wait_user_speak")
    zenbo.robot.set_expression(RobotFace.DEFAULT, timeout=5)
    slu_result = zenbo.robot.wait_for_listen(
        "",
        config={
            "listenLanguageId": 1,
        },
        timeout=120,
    )
    if not slu_result:
        return None
    zenbo_name = config["zenbo_name"]
    global been_called, keep_chat
    been_said = str(json.loads(slu_result.get("user_utterance"))[0].get("result")[0])
    if been_said == zenbo_name:
        welcome(zenbo, zenbo_name, been_called)
        been_called = True
        keep_chat = True
    elif been_said and keep_chat:
        zenbo.robot.set_expression(RobotFace.AWARE_RIGHT, timeout=5)
        reply_user_command(zenbo, been_said)
        keep_chat = False
    return slu_result


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
    response = lang.execute_command(command)
    zenbo.robot.set_expression(RobotFace.CONFIDENT_ADV, timeout=5)
    if response["action"] == "command":
        reply = response["comment"]
    elif response["action"] == "query":
        reply = response["summarize"]
    elif response["action"] == "answer":
        reply = response["answer"]
    elif response["action"] == "clarify":
        reply = response["question"]
    else:
        reply = "抱歉，我不太明白。"
    zenbo.robot.speak(reply)
