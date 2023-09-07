# coding:utf-8
import logging
import threading
from datetime import datetime

import pyzenbo
from pyzenbo.modules.dialog_system import RobotFace
from pyzenbo.modules.error_code import code_to_description

logging.basicConfig(level=logging.INFO)

# fill in zenbo junior's ip
host = '0.0.0.0'
sdk = pyzenbo.connect(host)

# domain UUID from DDE
domainUuid = "0101C61DBC204827AD186F99CEB572BB"

# domain ID from DDE
domainId = "16534"

# domain package from DDE
package_name = "com.asus.template.taipeiBus"

# domain version from DDE
version = "0.0.1"


def listen_callback(args):
    global event_listen

    slu_query = args.get('event_slu_query', None)
    if slu_query:
        print("slu_query=", slu_query)

        # get SLU semantic parts
        app_semantic = slu_query.get('app_semantic', None)
        if app_semantic:
            # printing SLU result
            print("app_semantic=", app_semantic)

            # use data (ex. intentionId) from SLU semantic parts to do followups
            intention_id = app_semantic.get('IntentionId', None)

            if intention_id:
                print("IntentionId=", intention_id)

                if intention_id == "taipeiBus.plan.user.startApp":
                    sdk.robot.speak('歡迎使用台北公車王，你想要查詢哪一班公車')
                    sdk.robot.speak_and_listen('你可以說紅13或紅35')

                if intention_id == "taipeiBus.plan.user.queryBusWhenArriveStation":
                    colorline = app_semantic.get('colorline1', "")
                    number = app_semantic.get('number1', "")
                    station = app_semantic.get('station1', "")
                    print('colorline:', colorline)
                    print('number:', number)
                    print('station:', station)
                    st = '這班車的時間如下'
                    print('TTS:', st)
                    sdk.robot.speak(st)
                    sdk.robot.speak('你可以說 Hey Zenbo 我要用台北公車王 重新測試')

                if intention_id == "taipeiBus.plan.user.querySpecificBus":
                    colorline = app_semantic.get('specificColorLine1', "")
                    number = app_semantic.get('specificNumber1', "")
                    print('colorline:', colorline)
                    print('number:', number)
                    st = '請問你要查甚麼資訊呢'
                    print('TTS:', st)
                    sdk.robot.speak(st)
                    sdk.robot.speak_and_listen('你可以說 出發時間或出發地點')

                if intention_id == "taipeiBus.plan.user.querySpecificBus.startStationAndTime":
                    sdk.robot.speak('這班車的資訊如下')
                    sdk.robot.speak('你可以說 Hey Zenbo '
                                    '紅13何時到關渡捷運站 或 我要用台北公車王 重新測試')

                if intention_id == "taipeiBus.plan.user.querySpecificBus.willPassSpecificPlaceOrNot":
                    location = app_semantic.get('location1', "")
                    print('location:', location)
                    st = '這班車不會經過' + location
                    print('TTS:', st)
                    sdk.robot.speak(st)
                    sdk.robot.speak('你可以說 Hey Zenbo '
                                    '紅13何時到關渡捷運站 或 我要用台北公車王 重新測試')

            if not event_listen.isSet():
                event_listen.set()
                print("event_listen.set")


def jump_to_plan_test():
    print('start jump_to_plan_test')
    sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
    sdk.robot.jump_to_plan(domainUuid, 'taipeiBus.plan.user.startApp')
    sdk.robot.speak_and_listen('你想查詢哪一班公車?')


sdk.robot.set_expression(RobotFace.DEFAULT, timeout=5)
# update domain corpus
sdk.robot.update_dialog_corpus_by_server(domainUuid, package_name, version)
sdk.robot.register_listen_callback(domainId, listen_callback)

try:
    print("starting")
    for i in range(5):
        print("第", i + 1, "句")
        event_listen = threading.Event()
        is_get_listening = event_listen.wait()
        sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)

finally:
    # release resources
    sdk.robot.stop_speak_and_listen()
    sdk.release()
