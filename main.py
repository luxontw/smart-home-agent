# import logging
# import websocket
# import helper
# from contextlib import suppress
# import _thread
# import time
# import rel


# import hass
# import lang
# from zenboclient import dialog, comm
# from pyzenbo.modules.dialog_system import RobotFace


# been_called = False
# config = helper.get_config()
# LOGGER = logging.getLogger("app")
# zenbo = comm.connect_robot(config["zenbo_ip"])
# zenbo.system.set_tts_volume(20)
# zenbo.robot.set_voice_trigger(False)
# zenbo.robot.set_expression(RobotFace.DEFAULT, timeout=5)


# def conn():
#     websocket.enableTrace(True)
#     websocket.setdefaulttimeout(600)
#     ws = websocket.WebSocketApp(
#         "ws://127.0.0.1:8765",
#         on_message=on_message,
#         on_error=on_error,
#         on_close=on_close,
#     )
#     ws.on_open = on_open
#     ws.run_forever(ping_timeout=600, dispatcher=rel, reconnect=5, skip_utf8_validation=True)
#     rel.signal(2, rel.abort)
#     rel.dispatch()


# def on_message(ws, message):
#     global been_called
#     LOGGER.info("STT module: %s", message)
#     dialog.reply_user_command(zenbo, message)
#     zenbo.robot.set_expression(RobotFace.DEFAULT, timeout=5)
#     # if config["zenbo_name"] == "助理":
#     #     been_called = True
#     # if been_called:
#     #     dialog.reply_user_command(zenbo, message)
#     #     been_called = False
#     # zenbo.robot.set_expression(RobotFace.DEFAULT, timeout=5)


# def on_error(ws, error):
#     LOGGER.info("STT module: %s", error)


# def on_close(ws):
#     LOGGER.info("STT module: closed")


# def on_open(ws):
#     LOGGER.info("STT module: opened")


# if __name__ == "__main__":
#     level = logging.DEBUG if config["debug"] else logging.INFO
#     logging.basicConfig(level=level)
#     with suppress(KeyboardInterrupt):
#         hass.init(config)
#         lang.init(config)
#         conn()
