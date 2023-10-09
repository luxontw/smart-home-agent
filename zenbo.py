import sys
import json
import logging

import llm
from functools import partial
from zenboclient import dialog, navigation, seeking, comm
from pyzenbo.modules.dialog_system import RobotFace


LOGGER = logging.getLogger()


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
        zenbo.robot.set_voice_trigger(False)
        listen_callback_handler = partial(dialog.handle_speak, zenbo)
        zenbo.robot.register_listen_callback(1207, listen_callback_handler)

        # Dialogue main logic
        while True:
            result = dialog.wait_user_speak(zenbo)
            if result:
                result = str(
                    json.loads(result.get("user_utterance"))[0].get("result")[0]
                )
                LOGGER.info("Stt result str: %s", result)
            if result == zenbo_name:
                command = dialog.welcome(zenbo, zenbo_name)
                zenbo.robot.speak("好的")
                LOGGER.debug("User command: %s", command)
                if command:
                    command = str(
                        json.loads(command.get("user_utterance"))[0].get("result")[0]
                    )
                    LOGGER.info("User command str: %s", command)
                    llm.execute_command(command)
                    zenbo.robot.set_expression(RobotFace.CONFIDENT_ADV, timeout=5)
                    zenbo.robot.speak("完成")

    except (KeyboardInterrupt, SystemExit):
        LOGGER.info("Stopping the program...")
        zenbo.release()
        sys.exit(0)
