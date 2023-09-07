import logging
import os
from pyzenbo.modules.dialog_system import RobotFace
import threading
import time

import pyzenbo
import pyzenbo.modules.zenbo_command as commands

logging.basicConfig(level=logging.INFO)
host = '0.0.0.0'


def demo_take_picture_and_file_transfer():
    with pyzenbo.connect(host) as sdk:
        event = threading.Event()

        def job(target_file):
            print('target_file', target_file)
            print('file_transmission', sdk.media.file_transmission(target_file))
            event.set()

        def file_transfer_test_on_result(**kwargs):
            print('on_result', kwargs)
            if kwargs.get('cmd') == commands.MEDIA_TAKE_PICTURE and kwargs.get(
                    'result') is not None:
                file = kwargs.get('result').get('file')
                print(file)
                t = threading.Thread(target=job, args=(os.path.basename(file),))
                t.start()

        sdk.on_result_callback = file_transfer_test_on_result
        print('take picture')
        sdk.media.take_picture(sync=False)
        if not event.wait(60):
            print('timeout exit')
            return
        print('exit')


if __name__ == '__main__':
    demo_take_picture_and_file_transfer()
