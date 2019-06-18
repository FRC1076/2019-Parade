import wpilib
import wpilib.drive
import ctre
from wpilib.interfaces import GenericHID

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        front_left_motor = wpilib.Talon(3) #TODO: Give correct values
        back_left_motor = wpilib.Talon(4) #TODO: Give correct values
        front_right_motor = wpilib.Talon(1) #TODO: Give correct values
        back_right_motor = wpilib.Talon(2) #TODO: Give correct values

        front_left_motor.setInverted(True)
        back_left_motor.setInverted(True)


        self.drive = wpilib.drive.MecanumDrive(front_left_motor,back_left_motor,front_left_motor,back_right_motor)
        self.drive.setExpiration(0.1)
        
        self.lstick = wpilib.Joystick(0)
        self.rstick = wpilib.Joystick(1)

        self.gyro = wpilib.AnalogGyro(1)

    def teleopInit(self):
        self.xforward = 0
        self.yforward = 0

    def teleopPeriodic(self):

        """Called when operation control mode is enabled"""

        
        self.drive.driveCartesian(
            self.lstick.getX(), self.lstick.getY(), self.rstick.getX(), self.gyro.getAngle()
        )
        
if __name__ == "__main__":
    wpilib.run(Robot,physics_enabled=True)