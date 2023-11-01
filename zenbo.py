import sys
import orjson as json
import logging

from functools import partial
from zenboclient import dialog, comm
from pyzenbo.modules.dialog_system import RobotFace


LOGGER = logging.getLogger("zenbo")


def init(config: dict):
    """
    Robot main logic
    """
    # Connect to the robot
    LOGGER.info("Set robot IP:  %s", config["zenbo_ip"])
    LOGGER.info("Set robot name:  %s", config["zenbo_name"])
    zenbo = comm.connect_robot(config["zenbo_ip"])
    zenbo_name = config["zenbo_name"]

    try:
        # Initialize
        zenbo.system.set_tts_volume(50)
        zenbo.robot.set_voice_trigger(False)
        listen_callback_handler = partial(dialog.listen_callback_handler, zenbo)
        zenbo.robot.register_listen_callback(1207, listen_callback_handler)

        # Dialogue main logic
        while True:
            LOGGER.info("Waiting for user command...")
            been_said = dialog.wait_user_speak(zenbo, config)
            LOGGER.info("slu_result: %s", been_said)

    except (KeyboardInterrupt, SystemExit):
        LOGGER.info("Stopping the program...")
        zenbo.release()
        sys.exit(0)
