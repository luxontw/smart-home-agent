import logging
import os

import pyzenbo.modules.inter_communication as _inter_comm
import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.baidu import Baidu
from pyzenbo.modules.dialog_system import DialogSystem
from pyzenbo.modules.inter_communication import DESTINATION
from pyzenbo.modules.line_follower import LineFollower
from pyzenbo.modules.media import Media
from pyzenbo.modules.motion import Motion
from pyzenbo.modules.sensor import Sensor
from pyzenbo.modules.system import System
from pyzenbo.modules.utility import Utility
from pyzenbo.modules.vision_control import VisionControl
from pyzenbo.modules.wheel_lights import WheelLights

logger = logging.getLogger('pyzenbo')


class PyZenbo:
    """
    Python Zenbo SDK, this SDK provides a interface to zenbo robot features.
    """
    _inter_comm = _inter_comm.InterComm()

    motion = Motion(_inter_comm)
    """
    Provides body movement and head control.

    :meth:`pyzenbo.modules.motion`
    """
    robot = DialogSystem(_inter_comm)
    """
    Class that can be used to make Zenbo speak and listen,
    and to change the facial expressions.

    :meth:`pyzenbo.modules.dialog\_system`
    """
    utility = Utility(_inter_comm)
    """
    Provides composite functions.

    :meth:`pyzenbo.modules.utility`
    """
    wheelLights = WheelLights(_inter_comm)
    """
    Control wheel lights.

    :meth:`pyzenbo.modules.wheel\_lights`
    """
    baidu = Baidu(_inter_comm)

    vision = VisionControl(_inter_comm)
    """
    Provides visual functions.

    :meth:`pyzenbo.modules.vision\_control`
    """
    lineFollower = LineFollower(_inter_comm)
    """
    Provides line follower control functions.

    :meth:`pyzenbo.modules.line\_follower`
    """
    sensor = Sensor(_inter_comm)
    """
    Provides sensor relate functions.

    :meth:`pyzenbo.modules.sensor`
    """
    system = System(_inter_comm)
    """
    Provides system relate functions.

    :meth:`pyzenbo.modules.system`
    """
    media = Media(_inter_comm)
    """
    Provides media relate functions.

    :meth:`pyzenbo.modules.media`
    """

    def __init__(self,
                 destination,
                 on_state_change_callback=None,
                 on_result_callback=None):
        if os.getenv('KEY_RUN_LOCALLY', 'false') == 'true':
            destination = '127.0.0.1'
        self._inter_comm.init((destination, 55555),
                              on_state_change_callback,
                              on_result_callback,
                              timeout=2)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.release()

    @property
    def on_state_change_callback(self):
        """
        Called when command state change in waiting queue.

        .. code-block:: python
            :caption: Usage

            def on_state_change(serial, cmd, error, state):
                msg = 'on_state_change serial:{}, cmd:{}, error:{}, state:{}'
                print(msg.format(serial, cmd, \
error_code.code_to_description(error), state))

            sdk = pyzenbo.connect(host_ip)
            sdk.on_state_change_callback = on_state_change
        """
        return self._inter_comm.on_state_change_callback

    @on_state_change_callback.setter
    def on_state_change_callback(self, on_state_change_callback):
        logger.debug(self._inter_comm.on_state_change_callback)
        self._inter_comm.on_state_change_callback = on_state_change_callback
        logger.debug(self._inter_comm.on_state_change_callback)

    @on_state_change_callback.deleter
    def on_state_change_callback(self):
        del self._inter_comm.on_state_change_callback

    @property
    def on_result_callback(self):
        """
        Called when a robot command sending result.

        .. code-block:: python
            :caption: Usage

            def on_result(**kwargs):
                print('on_result', kwargs)

            sdk = pyzenbo.connect(host_ip)
            sdk.on_result_callback = on_result
        """
        return self._inter_comm.on_result_callback

    @on_result_callback.setter
    def on_result_callback(self, on_result_callback):
        self._inter_comm.on_result_callback = on_result_callback

    @on_result_callback.deleter
    def on_result_callback(self):
        del self._inter_comm.on_result_callback

    @property
    def on_vision_callback(self):
        """
        Called when vision service sending result.

        .. code-block:: python
            :caption: Usage

            def on_vision_callback(**kwargs):
                print('on_vision_callback', kwargs)

            sdk = pyzenbo.connect(host_ip)
            sdk.on_vision_callback = on_vision_callback
        """
        return self._inter_comm.on_vision_callback

    @on_vision_callback.setter
    def on_vision_callback(self, on_vision_callback):
        self._inter_comm.on_vision_callback = on_vision_callback

    @on_vision_callback.deleter
    def on_vision_callback(self):
        del self._inter_comm.on_vision_callback

    def release(self):
        """
        Release all robot API resource. After finished using SDK,
        must call this function to disconnect the connection.

        :return: None
        """
        logger.info('PyZenboSDK prepare release, cancel all command')
        self._inter_comm.release()
        logger.info('PyZenboSDK released')

    def cancel_command(self, command, sync=True, timeout=None):
        """
        Cancel specific robot motion/utility command.

        .. code-block:: python
            :caption: Usage

            sdk = pyzenbo.connect(host_ip)
            sdk.motion.move_body(10, 0, 0, 2, sync=False)
            sdk.cancel_command(zenbo_command.MOTION_MOVE_BODY)

        :param command: specifies the command number to cancel
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["coordinator"]
        cmd = commands.CANCEL
        data = {
            'command': int(command),
            'target_id': 0,
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def cancel_command_by_serial(self, serial, sync=True, timeout=None):
        """
        Cancel specific robot motion/utility command by using the serial
        number.

        .. code-block:: python
            :caption: Usage

            sdk = pyzenbo.connect(host_ip)
            serial = sdk.motion.move_body(10, 0, 0, 2, sync=False)[0]
            sdk.cancel_command_by_serial(serial)

        :param serial: specifies the command serial number to cancel
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["coordinator"]
        cmd = commands.CANCEL
        data = {
            'command': 0,
            'target_id': int(serial),
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def cancel_command_all(self, sync=True, timeout=None):
        """
        Cancel all robot motion/utility commands

        .. code-block:: python
            :caption: Usage

            sdk = pyzenbo.connect(host_ip)
            sdk.motion.move_body(10, 0, 0, 2, sync=False)
            sdk.cancel_command_all()

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["coordinator"]
        cmd = commands.CANCEL
        data = {
            'command': 0,
            'target_id': 0,
        }
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def get_connection_state(self):
        """
        Get current connection state.

        | Socket state
        |   Init: 0
        |   Connected: 1
        |   Disconnected: 2
        |   Retry_1: 3
        |   Retry_2: 4
        |   Retry_3: 5
        |   Failed: 6
        |   Closed: 7

        :return: a tuple it contain sender state and receive state
        """
        return self._inter_comm.skt.stateSend, \
            self._inter_comm.skt.stateReceive


def main():
    pass


if __name__ == '__main__':
    main()
