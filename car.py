

class Car:

    def __init__(self, left_motor, right_motor, right_motor_correction_speed = 1, left_motor_correction_speed= 1):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.right_motor_correction_speed = right_motor_correction_speed
        self.left_motor_correction_speed = left_motor_correction_speed
