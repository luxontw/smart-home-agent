# coding:utf-8
import logging
import random
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
domainUuid = "346241F0B8984AD09CD921ED8E52B9FA"

# domain ID from DDE
domainId = "16486"

# domain package from DDE
package_name = "com.asus.ds.tangpoetry"

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

                if intention_id == "plan_lanuchAPP":
                    sdk.robot.speak('歡迎使用唐詩三百首')

                if intention_id == "plan_listen_poet":
                    poet = app_semantic.get('poet', "")
                    type = app_semantic.get('type', "")
                    title = app_semantic.get('title', "")
                    print('poet:', poet)
                    st = "為您播放" + poet + "的詩"
                    sdk.robot.speak(st)

                if intention_id == "plan_listen_title":
                    title = app_semantic.get('title', "")
                    print('title:', title)
                    st = "為您播放" + title
                    sdk.robot.speak(st)

                if intention_id == "plan_listen_combo":
                    poet = app_semantic.get('poet', "")
                    title = app_semantic.get('title', "")
                    print('poet:', poet)
                    print('title:', title)
                    st = "為您播放" + poet + "的" + title
                    sdk.robot.speak(st)

                if intention_id == "plan_listen_any":
                    any = app_semantic.get('any', "")
                    print('any:', any)
                    st = "收到" + any
                    sdk.robot.speak(st)

                if intention_id == "plan_listen_any_one":
                    sdk.robot.speak("為您隨便播放一首")

                if intention_id == "plan_listen_next_one":
                    sdk.robot.speak("為您播放下一首")

                if intention_id == "plan_listen_type":
                    type = app_semantic.get('type', "")
                    print('type:', type)
                    st = "為您播放" + type
                    sdk.robot.speak(st)

                if intention_id == "plan_stopRecite":
                    sdk.robot.speak("收到暫停")

                if intention_id == "plan_continue":
                    sdk.robot.speak("收到繼續")

                if intention_id == "plan_launchAPPversion":
                    sdk.robot.speak("顯示版本資訊")

                sentence_list = [
                    "白居易的詩", "隨便一個", "來首七言律詩", "孟浩然的過故人莊", "來個月下獨酌"
                ]
                st = "你可以說, 嘿小布, " + random.choice(sentence_list)
                sdk.robot.speak(st)

            if not event_listen.isSet():
                event_listen.set()
                print("event_listen.set")


def jump_to_plan_test():
    print('start jump_to_plan_test')
    sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
    sdk.robot.jump_to_plan(domainUuid, 'plan_lanuchAPP')
    sdk.robot.speak_and_listen('想聽哪一首詩呢')


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
