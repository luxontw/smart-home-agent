import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.inter_communication import DESTINATION


class System:

    def __init__(self, inter_comm):
        self._inter_comm = inter_comm

    def get_ac_plug_status(self, sync=True, timeout=None):
        """
        Get current AC-plug status, the result is returned by
         on_result_callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["system"]
        cmd = commands.SYSTEM_AC_PLUG_STATUS_GET
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def register_ac_plug_status(self, sync=True, timeout=None):
        """
        Register the AC-plug status callback, the result is returned by
        on_result_callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_AC_PLUG_STATUS_REGISTER
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def unregister_ac_plug_status(self, sync=True, timeout=None):
        """
        Unregister the AC-plug status callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_AC_PLUG_STATUS_UNREGISTER
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def get_battery_status(self, sync=True, timeout=None):
        """
        Get current battery status, the result is returned
        by on_result_callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["system"]
        cmd = commands.SYSTEM_BATTERY_STATUS_GET
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def register_battery_status(self, sync=True, timeout=None):
        """
        Register the battery status callback, the result is returned by
        on_result_callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_BATTERY_STATUS_REGISTER
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def unregister_battery_status(self, sync=True, timeout=None):
        """
        Unregister the battery status callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_BATTERY_STATUS_UNREGISTER
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def register_battery_status_event(self,
                                      operator,
                                      value,
                                      sync=True,
                                      timeout=None):
        """
        Register the battery status event callback, when battery level reach
        the condition that specified, the result is returned by
        on_result_callback.

        :param operator: comparison type with a threshold value.
            0: = (Equal)
            1: ≠ (Not Equal)
            2: > (Greater Than)
            3: ≥ (Greater Than or Equal To)
            4: < (Less Than)
            5: ≤ (Less Than or Equal To)
        :param value: threshold value to compare sensor data
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_BATTERY_STATUS_EVENT_REGISTER
        data = {'operator': int(operator), 'value': float(value)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def unregister_battery_status_event(self,
                                        operator,
                                        value,
                                        sync=True,
                                        timeout=None):
        """
        Unregister the battery status event callback.

        :param operator: comparison type with a threshold value.
            0: = (Equal)
            1: ≠ (Not Equal)
            2: > (Greater Than)
            3: ≥ (Greater Than or Equal To)
            4: < (Less Than)
            5: ≤ (Less Than or Equal To)
        :param value: threshold value to compare sensor data
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_BATTERY_STATUS_EVENT_UNREGISTER
        data = {'operator': int(operator), 'value': float(value)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def get_media_volume(self, sync=True, timeout=None):
        """
        Get current media volume level, the result is
        returned by on_result_callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["system"]
        cmd = commands.SYSTEM_MEDIA_VOLUME_GET
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def set_media_volume(self, value, sync=True, timeout=None):
        """
        Set media volume level.

        :param value: value can be 'UP', 'DOWN' or decimal between 0 and 100
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["system"]
        cmd = commands.SYSTEM_MEDIA_VOLUME_SET
        data = {'value': str(value).upper()}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def get_tts_volume(self, sync=True, timeout=None):
        """
        Get current text to speech volume level, the result is returned by
        on_result_callback.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["system"]
        cmd = commands.SYSTEM_TTS_VOLUME_GET
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def set_tts_volume(self, value, sync=True, timeout=None):
        """
        Set text to speech volume level.

        :param value: value can be 'UP', 'DOWN' or decimal between 0 and 100
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["system"]
        cmd = commands.SYSTEM_TTS_VOLUME_SET
        data = {'value': str(value).upper()}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def register_screen_touch_event(self,
                                    event_type,
                                    value,
                                    sync=True,
                                    timeout=None):
        """
        Register the screen touch event callback, the result is returned by
        on_result_callback.

        :param event_type:
            0: All event type
            1: finger touch
            2: swipe up
            3: swipe down
            4: swipe left
            5: swipe right
        :param value: how many fingers touch the screen, decimal between
            0 and 10
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_SCREEN_TOUCH_EVENT_REGISTER
        data = {'event_type': int(event_type), 'value': int(value)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def unregister_screen_touch_event(self,
                                      event_type,
                                      value,
                                      sync=True,
                                      timeout=None):
        """
        Unregister the screen touch event callback.

        :param event_type:
            0: All event type
            1: finger touch
            2: swipe up
            3: swipe down
            4: swipe left
            5: swipe right
        :param value: how many fingers touch the screen, decimal between
            0 and 10
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION['system']
        cmd = commands.SYSTEM_SCREEN_TOUCH_EVENT_UNREGISTER
        data = {'event_type': int(event_type), 'value': int(value)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error
