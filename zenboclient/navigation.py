"""
Navigation-related functions to move Zenbo around the room.
"""
import pyzenbo

from pyzenbo.modules.dialog_system import RobotFace

def dance(zenbo: pyzenbo.PyZenbo, reply:str):
    zenbo.robot.speak(reply)
    for i in range(8):
        zenbo.robot.set_expression(RobotFace.SINGING_ADV, timeout=5)
        zenbo.wheelLights.start_glowing_yoyo(0, 0, True, 10)
        zenbo.motion.move_body(0, 0, -90, 10, True, 10)
def sleep(zenbo: pyzenbo.PyZenbo):
    zenbo.robot.set_expression(RobotFace.LAZY, timeout=5)