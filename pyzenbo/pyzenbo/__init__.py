from .modules import error_code, zenbo_command
from .modules.inter_communication import STATE
from .modules.line_follower import LineFollowerConfig
from .py_zenbo_sdk import PyZenbo

__version__ = '1.0.46.2220'


def connect(destination,
            on_state_change_callback=None,
            on_result_callback=None):
    return PyZenbo(destination, on_state_change_callback, on_result_callback)
