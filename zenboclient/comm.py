import pyzenbo
from pyzenbo.modules.error_code import code_to_description


def on_state_change(serial, cmd, error, state):
    msg = 'on_state_change serial:{}, cmd:{}, error:{}, state:{}'
    print(msg.format(serial, cmd, error, state))
    if error:
        print("on_state_change error:", code_to_description(error))

def connect_robot(ip) -> pyzenbo.PyZenbo:
    print('Connecting to the robot ({})...'.format(ip))
    return pyzenbo.connect(ip, on_state_change)