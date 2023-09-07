import logging

import pyzenbo
from pyzenbo.modules.dialog_system import RobotFace
from pyzenbo.modules.error_code import code_to_description

logging.basicConfig(level=logging.INFO)
host = '0.0.0.0'
sdk = pyzenbo.connect(host)
domain_id = "1303"
domain_uuid = 'E7AABB554ACB414C9AB9BF45E7FA8AD9'
timeout = 15


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
        'Which city do you like? You can say Hello Block City, or Hello White City',
        config={
            'listenLanguageId': 2,
        })
    return slu_result


def not_found():
    print('not_found')
    sdk.robot.set_expression(RobotFace.TIRED, timeout=5)
    sdk.robot.speak('No one is here')


sdk.on_state_change_callback = on_state_change
sdk.robot.register_listen_callback(domain_id, listen_callback)
sdk.robot.set_expression(RobotFace.HIDEFACE, timeout=5)

try:
    result = sdk.vision.wait_for_detect_face(enable_debug_preview=True,
                                             timeout=timeout)
    print('wait_for_detect_face result:', result)
    if result:
        slu = say_hello_and_ask()
        print('say_hello_and_ask result:', slu)
    else:
        not_found()
    sdk.robot.set_expression(RobotFace.HIDEFACE, timeout=5)
finally:
    print("exit")
    sdk.robot.stop_speak_and_listen()
    sdk.vision.cancel_detect_face()
    sdk.release()
