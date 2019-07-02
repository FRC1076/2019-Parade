import wpilib
import ctre
from wpilib.interfaces import GenericHID
from wpilib.drive import DifferentialDrive

LEFT_HAND = GenericHID.Hand.kLeft
RIGHT_HAND = GenericHID.Hand.kRight

class Robot(wpilib.TimedRobot):
    def robotInit(self):
        #TODO: get real numbers for the talons
        self.frontLeft = ctre.WPI_TalonSRX(1)
        self.rearLeft = ctre.WPI_TalonSRX(2)
        self.left = wpilib.SpeedControllerGroup(self.frontLeft, self.rearLeft)

        self.frontRight = ctre.WPI_TalonSRX(3)
        self.rearRight = ctre.WPI_TalonSRX(4)
        self.right = wpilib.SpeedControllerGroup(self.frontRight, self.rearRight)

        self.drivetrain = wpilib.drive.DifferentialDrive(self.left, self.right)

        self.controller = wpilib.XboxController(0) #TODO: get actual port of controller

    def robotPeriodic(self):
        return

    def teleopInit(self):
        print("TELEOP BEGINS")

    def teleopPeriodic(self):
        #TODO: add a deadzone to not kill the driver
        #TODO: figure out what values should be negative
        leftSpeed = deadzone(self.controller.getY(LEFT_HAND), 0.2)
        rightSpeed = deadzone(self.controller.getRawAxis(3), 0.2)
        
        if self.controller.getXButton():
            leftSpeed = 0
            rightSpeed = 0

        self.drivetrain.tankDrive(leftSpeed, rightSpeed)

def deadzone(val, deadzone):
    if abs(val) < deadzone:
        return 0
    elif val < (0):
        x = ((abs(val) - deadzone)/(1-deadzone))
        return (-x)
    else:
        x = ((val - deadzone)/(1-deadzone))
        return (x)

if __name__ == "__main__":
	wpilib.run(Robot, physics_enabled = True)
