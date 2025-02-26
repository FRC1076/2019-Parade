#
# See the documentation for more details on how this works
#
# The idea here is you provide a simulation object that overrides specific
# pieces of WPILib, and modifies motors/sensors accordingly depending on the
# state of the simulation. An example of this would be measuring a motor
# moving for a set period of time, and then changing a limit switch to turn
# on after that period of time. This can help you do more complex simulations
# of your robot code without too much extra effort.
#


#
# See the notes for the other physics sample
#


from pyfrc.physics import drivetrains


class PhysicsEngine(object):
    """
       Simulates a 4-wheel mecanum robot using Tank Drive joystick control 
    """

    def __init__(self, physics_controller):
        """
            :param physics_controller: `pyfrc.physics.core.Physics` object
                                       to communicate simulation effects to
        """

        self.physics_controller = physics_controller

    def update_sim(self, hal_data, now, tm_diff):
        """
            Called when the simulation parameters for the program need to be
            updated.
            
            :param now: The current time as a float
            :param tm_diff: The amount of time that has passed since the last
                            time that this function was called
        """

        # Simulate the drivetrain
        # -> Remember, in the constructor we inverted the left motors, so
        #    invert the motor values here too!
        lr_motor = -hal_data["pwm"][1]["value"]
        rr_motor = hal_data["pwm"][2]["value"]
        lf_motor = -hal_data["pwm"][3]["value"]
        rf_motor = hal_data["pwm"][4]["value"]

        vx, vy, vw = drivetrains.mecanum_drivetrain(
            lr_motor, rr_motor, lf_motor, rf_motor
        )
        self.physics_controller.vector_drive(vx, vy, vw, tm_diff)