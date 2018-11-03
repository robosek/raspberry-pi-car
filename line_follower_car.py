from gpiozero import LineSensor
from car import Car


class LineFollowerCar(Car):

    def __init__(self, left_motor, right_motor, speed = 1,right_motor_correction_speed=1, left_motor_correction_speed=1):
        super().__init__(left_motor, right_motor, right_motor_correction_speed, left_motor_correction_speed)
        self.left_sensor = LineSensor(23)
        self.right_sensor = LineSensor(24)
        self.speed = speed

    def move(self):
        left_mot = 0
        right_mot = 0
        while True:
            left_detect = int(self.left_sensor.value)
            right_detect = int(self.right_sensor.value)
            if left_detect == 0 and right_detect == 0:
                left_mot = 1
                right_mot = 1
            if left_detect == 0 and right_detect == 1:
                left_mot = -1
            if left_detect == 1 and right_detect == 0:
                right_mot = -1
            self.right_motor.forward(right_mot * self.speed)
            self.left_motor.forward(left_mot * self.speed)

    def stop(self):
        self.right_motor.stop()
        self.left_motor.stop()
        self.right_sensor.close()
        self.left_sensor.close()
