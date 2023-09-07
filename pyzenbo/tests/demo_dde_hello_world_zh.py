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
domainUuid = "BFC8C1C022F348BAA6459EB3E6E8EC8D"

# domain ID from DDE
domainId = "16660"

# domain package from DDE
package_name = "com.asus.zenbodialogsample"

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

                if intention_id == "lanuchHelloWolrd_Plan":
                    sdk.robot.speak('哈囉我是Zenbo, 很高興認識你')
                    sdk.robot.speak('你喜歡哪個城市, 你可以說 哈囉黑色城市 或是 哈囉白色城市')
                    sdk.robot.speak_and_listen("")

                if intention_id == "helloWorld":
                    # parse city
                    city_name = app_semantic.get('myCity1', None)
                    # TTS
                    sdk.robot.speak('你現在位於' + str(city_name))

            if not event_listen.isSet():
                event_listen.set()
                print("event_listen.set")


def jump_to_plan_test():
    print('start jump_to_plan_test')
    sdk.robot.set_expression(RobotFace.HAPPY, timeout=5)
    sdk.robot.jump_to_plan(domainUuid, 'lanuchHelloWolrd_Plan')
    sdk.robot.speak('哈囉我是Zenbo, 很高興認識你')
    sdk.robot.speak_and_listen('你喜歡哪個城市, 你可以說 哈囉黑色城市 或是 哈囉白色城市')


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
