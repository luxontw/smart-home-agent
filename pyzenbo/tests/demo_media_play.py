import logging
import os
import threading
import time

import pyzenbo
import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.error_code import code_to_description

logging.basicConfig(level=logging.INFO)
host = '0.0.0.0'


def on_state_change(serial, cmd, error, state):
    fmt = 'on_state_change serial:{}, cmd:{}, error:{}, state:{}'
    print(fmt.format(serial, cmd, error, state))
    if error:
        print('on_state_change error:', code_to_description(error))


def demo_take_picture_and_play(sdk):
    event = threading.Event()

    def job(target_file):
        print('target_file', target_file)
        file_path, file_name = os.path.split(target_file)
        print('play_media', sdk.media.play_media(file_path, file_name, False))
        time.sleep(5)
        event.set()

    def file_transfer_test_on_result(**kwargs):
        print('on_result', kwargs)
        if kwargs.get('cmd') == commands.MEDIA_TAKE_PICTURE and kwargs.get(
                'result') is not None:
            file = kwargs.get('result').get('file')
            print('record file', file)
            t = threading.Thread(target=job, args=(file,))
            t.start()

    sdk.on_result_callback = file_transfer_test_on_result
    print('take picture')
    sdk.media.take_picture(sync=False)
    if not event.wait(15):
        print('timeout exit')
        return
    print('exit')


def demo_media_record_and_play(sdk):
    event = threading.Event()

    def job(target_file):
        print('target_file', target_file)
        file_path, file_name = os.path.split(target_file)
        print('play_media', sdk.media.play_media(file_path, file_name))
        event.set()

    def stop_record_job(delay):
        time.sleep(delay)
        print('stop record')
        sdk.media.stop_record_video()

    def on_result(**kwargs):
        print('on_result', kwargs)
        if (kwargs.get('cmd') == commands.MEDIA_RECORD_VIDEO or
                kwargs.get('cmd') == commands.MEDIA_STOP_RECORD_VIDEO
           ) and kwargs.get('result') is not None:
            file = kwargs.get('result').get('file')
            print('record file', file)
            t = threading.Thread(target=job, args=(file,))
            t.start()

    sdk.on_state_change_callback = on_state_change
    sdk.on_result_callback = on_result

    duration_time = 15
    print('record_video')
    result = sdk.media.record_video(duration_time, sync=False)
    print(result)
    t = threading.Thread(target=stop_record_job, args=(10,))
    t.start()
    if not event.wait(60):
        print('timeout exit')
        return
    print('exit')


if __name__ == '__main__':
    with pyzenbo.connect(host, on_state_change) as sdk:
        demo_media_record_and_play(sdk)
        demo_take_picture_and_play(sdk)
