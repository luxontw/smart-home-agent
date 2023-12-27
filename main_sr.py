import logging
import helper
import speech_recognition as sr
from contextlib import suppress

import hass
import lang
from zenboclient import dialog, comm
from pyzenbo.modules.dialog_system import RobotFace

r = sr.Recognizer()
config = helper.get_config()
LOGGER = logging.getLogger("app")
zenbo = comm.connect_robot(config["zenbo_ip"])
zenbo.system.set_tts_volume(50)
zenbo.robot.set_voice_trigger(False)
zenbo.robot.set_expression(RobotFace.DEFAULT, timeout=5)

mic = sr.Microphone(device_index=0)

def get_speech_recognition():
    with mic as source:
        print("Listening...")
        try:
            audio_data = r.listen(source=source, timeout=5)
            text = r.recognize_google(audio_data, language="zh-TW")
            print(text)
        except:
            text = ""
        return text


if __name__ == "__main__":
    level = logging.DEBUG if config["debug"] else logging.INFO
    logging.basicConfig(level=level)
    with suppress(KeyboardInterrupt):
        hass.init(config)
        lang.init(config)
        while True:
            result = get_speech_recognition()
            LOGGER.info("STT result:|%s|", result)
            if result != "":
                dialog.reply_user_command(zenbo, result)
                zenbo.robot.set_expression(RobotFace.DEFAULT, timeout=5)
