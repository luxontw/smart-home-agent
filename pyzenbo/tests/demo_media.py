import logging
import os
import threading

import pyzenbo
import pyzenbo.modules.zenbo_command as commands
from pyzenbo.modules.error_code import code_to_description

logging.basicConfig(level=logging.INFO)
host = '0.0.0.0'


def demo_record_audio():
    with pyzenbo.connect(host) as sdk:
        event = threading.Event()

        def job(target_file):
            print('target_file', target_file)
            file_path, file_name = os.path.split(target_file)
            print('play_media', sdk.media.play_media(file_path, file_name))
            print('file_transmission', sdk.media.file_transmission(file_name))
            event.set()

        def on_state_change(serial, cmd, error, state):
            fmt = 'on_state_change serial:{}, cmd:{}, error:{}, state:{}'
            print(fmt.format(serial, cmd, error, state))
            if error:
                print('on_state_change error:', code_to_description(error))

        def on_result(**kwargs):
            print('on_result', kwargs)
            if kwargs.get('cmd') == commands.MEDIA_RECORD_AUDIO and kwargs.get(
                    'result') is not None:
                file = kwargs.get('result').get('file')
                print(file)
                t = threading.Thread(target=job, args=(file,))
                t.start()

        sdk.on_state_change_callback = on_state_change
        sdk.on_result_callback = on_result

        duration_time = 10
        print('record_audio')
        result = sdk.media.record_audio(duration_time, sync=False)
        print(result)
        if not event.wait(60):
            print('timeout exit')
            return
        print('exit')


if __name__ == '__main__':
    demo_record_audio()
