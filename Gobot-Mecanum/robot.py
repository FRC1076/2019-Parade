import wpilib
import wpilib.drive
import ctre
import robotmap

class Robot(wpilib.TimedRobot):

    def robotInit(self):
        front_left_motor = robotmap.motor(robotmap.mecanum['front_left_motor']) #TODO: Give correct values
        back_left_motor = robotmap.motor(robotmap.mecanum['back_left_motor']) #TODO: Give correct values
        front_right_motor = robotmap.motor(robotmap.mecanum['front_right_motor']) #TODO: Give correct values
        back_right_motor = robotmap.motor(robotmap.mecanum['back_left_motor']) #TODO: Give correct values

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
            self.lstick.getX, self.lstick.getY(), self.rstick.getX(), self.gyro.getAngle()
        )

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
    wpilib.run(Robot,physics_enabled=True)