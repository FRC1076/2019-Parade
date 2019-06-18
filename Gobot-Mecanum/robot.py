import wpilib
import wpilib.drive
import ctre
from wpilib.interfaces import GenericHID

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        front_left_motor =ctre.WPI_TalonSRX(3) #TODO: Give correct values
        back_left_motor = ctre.WPI_TalonSRX(4) #TODO: Give correct values
        front_right_motor = ctre.WPI_TalonSRX(1) #TODO: Give correct values
        back_right_motor = ctre.WPI_TalonSRX(2) #TODO: Give correct values

        front_left_motor.setInverted(True)
        back_left_motor.setInverted(True)


        self.drive = wpilib.drive.MecanumDrive(front_left_motor,back_left_motor,front_left_motor,back_right_motor)
        self.drive.setExpiration(0.1)
        
        self.lstick = wpilib.Joystick(0)
        self.rstick = wpilib.Joystick(1)

    def teleopInit(self):
        self.xforward = 0
        self.yforward = 0

    def teleopPeriodic(self):

        """Called when operation control mode is enabled"""

       
        self.drive.driveCartesian(
            self.lstick.getX(), self.lstick.getY(), self.rstick.getX(), 0
        )
        
if __name__ == "__main__":
    wpilib.run(Robot,physics_enabled=True)