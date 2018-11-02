from gpiozero import Motor


class Car:

    def __init__(self, right_motor_correction_speed = 1, left_motor_correction_speed= 1):
        self.left_motor = Motor(22, 27)
        self.right_motor = Motor(26, 17)
        self.right_motor_correction_speed = right_motor_correction_speed
        self.left_motor_correction_speed = left_motor_correction_speed
