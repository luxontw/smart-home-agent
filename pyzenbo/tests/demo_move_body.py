import logging

import pyzenbo
from pyzenbo.modules.error_code import code_to_description

logging.basicConfig(level=logging.INFO)
host = '0.0.0.0'


def on_state_change(serial, cmd, error, state):
    msg = 'on_state_change serial:{}, cmd:{}, error:{}, state:{}'
    print(msg.format(serial, cmd, error, state))
    if error:
        print('on_state_change error:', code_to_description(error))


def on_result(**kwargs):
    print('on_result', kwargs)


with pyzenbo.connect(host) as sdk:
    sdk.on_state_change_callback = on_state_change
    sdk.on_result_callback = on_result

    result = sdk.motion.move_body(0.4, 0, 0, sync=False, timeout=None)
    print(result)
    result = sdk.motion.move_body(-0.4, 0, 0, sync=True, timeout=100)
    print(result)
