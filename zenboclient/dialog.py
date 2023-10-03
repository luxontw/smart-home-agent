"""
Voice recognition and dialog related functions to interact between Zenbo
and the user.
"""
import pyzenbo
import json
from pyzenbo.modules.dialog_system import RobotFace

def handle_speak(zenbo: pyzenbo.PyZenbo, args):
    """
    Handles user speaking -- whenever user says something, Zenbo calls this function.
    """
    event_user_utterance = args.get('event_user_utterance', None)
    name =  "小布"
    if event_user_utterance:
        been_said = str(json.loads(event_user_utterance.get('user_utterance'))[0].get('result')[0])
        print("been_said: ", been_said)
        if been_said == '中文辨識':
            zenbo.robot.speak("請說出您想要的功能")
            zenbo.motion.move_body(0.15, speed_level=2)
        if been_said == '名稱設定':
            zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
            slu_result = zenbo.robot.wait_for_listen(
            "請說出您要設定的名字?",
                config={
                    "listenLanguageId":1,
                },
             )
            name = str(json.loads(slu_result.get('event_user_utterance').get('user_utterance'))[0].get('result')[0])
        if  been_said == name:
            welcome(zenbo)


def ask_user_for_play(zenbo: pyzenbo.PyZenbo):
    """
    Asks the user if he/she wants to play some hide and seek.
    """
    print("ask_user_for_play")
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    slu_result = zenbo.robot.wait_for_listen(
        "",
        config={
            "listenLanguageId":1,
        },
    )
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    return slu_result

def welcome(zenbo: pyzenbo.PyZenbo):
    """
    Asks the user if he/she wants to play some hide and seek.
    """
    print("ask_user_for_play")
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    zenbo.robot.speak("你好我是小布，很高興認識你。") 
    slu_result = zenbo.robot.wait_for_listen(
        "需要什麼協助嗎?",
        config={
            "listenLanguageId":1,
        },
    )
    zenbo.robot.set_expression(RobotFace.HAPPY, timeout=5)
    return slu_result

def say_fine(zenbo: pyzenbo.PyZenbo):
    """
    FFFFINE.
    """
    zenbo.robot.speak('Fine.')