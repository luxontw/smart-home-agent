import logging

import pyzenbo
from pyzenbo.modules.dialog_system import RobotFace

logging.basicConfig(level=logging.INFO)
host = '0.0.0.0'

sdk = pyzenbo.connect(host)
sdk.robot.set_expression(RobotFace.HAPPY, 'Hello World')
sdk.robot.set_expression(RobotFace.HIDEFACE)

sdk.release()
