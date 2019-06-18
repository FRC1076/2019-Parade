import ctre

def motor(value):
    ctre.WPI_TalonSRX(value)

mecanum = {
    'front_left_motor': 3,
    'back_left_motor': 4,
    'front_right_motor': 1,
    'back_right_motor': 2

}
