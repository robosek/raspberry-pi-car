class LineFollowerCar:

    def __init__(self, car, left_sensor, right_sensor, speed = 1):
        self.car = car
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor
        self.speed = speed

    def move(self):
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
            self.car.right_motor.forward(right_mot * self.speed)
            self.car.left_motor.forward(left_mot * self.speed)

    def stop(self):
        self.car.right_motor.stop()
        self.car.left_motor.stop()
        self.right_sensor.close()
        self.left_sensor.close()
