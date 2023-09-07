import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.inter_communication import DESTINATION


class Media:

    def __init__(self, inter_comm):
        self._inter_comm = inter_comm

    def take_picture(self, sync=True, timeout=None):
        """
        Take picture.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_TAKE_PICTURE
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def record_video(self, duration, sync=True, timeout=None):
        """
        Record video.

        :param duration: the time during record video in seconds
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_RECORD_VIDEO
        data = {'duration': int(duration)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def stop_record_video(self, sync=True, timeout=None):
        """
        Stop record video.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_STOP_RECORD_VIDEO
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def record_audio(self, duration, sync=True, timeout=None):
        """
        Record audio.

        :param duration: the time during record video in seconds
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_RECORD_AUDIO
        data = {'duration': int(duration)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def stop_record_audio(self, sync=True, timeout=None):
        """
        Stop record audio.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_STOP_RECORD_AUDIO
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def play_media(self, file_path, file_name, sync=True, timeout=None):
        """
        Play media.

        :param file_path: file path in Zenbo junior storage
        :param file_name: file name in Zenbo junior storage
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_PLAY_MEDIA
        data = {'filePath': str(file_path), 'fileName': str(file_name)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def stop_media(self, file_path="", file_name="", sync=True, timeout=None):
        """
        Stop play media. If file_path and file_name are empty strings,
        all play media will be stopped.

        :param file_path: file path in Zenbo junior storage
        :param file_name: file name in Zenbo junior storage
        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_STOP_MEDIA
        data = {'filePath': str(file_path), 'fileName': str(file_name)}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def get_file_list(self, sync=True, timeout=None):
        """
        Get media file list store in Zenbo lab.

        :param sync: True if this command is blocking
        :param timeout: maximum blocking time in second, None means infinity
        :return: serial number of the command, if command is blocking also
            return a dict, it include two key, 'state' indicate execute
            result and 'error' will contain error code
        """
        des = DESTINATION["media"]
        cmd = commands.MEDIA_GET_FILE_LIST
        data = {}
        serial, error = self._inter_comm.send_command(des, cmd, data, sync,
                                                      timeout)
        return serial, error

    def file_transmission(self, target_file, over_write=False):
        """
        Media file transfer, this file will store in working directory.

        :param target_file: target file name
        :param over_write: overwrite existing file
        :return: file name and file size if transfer success, otherwise
            return error message ('EXIST_FILE_NAME' or 'WRONG_FILE_NAME') and 0
        """
        return self._inter_comm.file_transfer(target_file, over_write)
