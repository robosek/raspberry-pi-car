from gpiozero import LineSensor
from car import Car
import time
from signal import pause

class LineFollowerCar(Car):

    def __init__(self, left_motor, right_motor, speed = 1,right_motor_correction_speed=1, left_motor_correction_speed=1):
        super().__init__(left_motor, right_motor, right_motor_correction_speed, left_motor_correction_speed)
        self.right_sensor = LineSensor(24, threshold=0.9)
        self.speed = speed
        self.ride = False
        
    def try_to_find_line(self):
        self.backward()
        time.sleep(0.3)
        self.left()
        time.sleep(0.3)
        self.right()
        time.sleep(0.3)
        self.right_motor.stop()
        self.left_motor.stop()
        time.sleep(0.3)
        if not self.ride:
            self.stop()
        
    def forward(self):
        self.right_motor.forward(self.speed)
        self.left_motor.forward(self.speed)
        if not self.ride:
            self.stop()
    
    def backward(self):
        self.right_motor.backward(self.speed)
        self.left_motor.backward(self.speed)

    def left(self):
        self.right_motor.forward(self.speed)
        self.left_motor.backward(self.speed)

    def right(self):
        self.right_motor.backward(self.speed)
        self.left_motor.forward(self.speed  * 1.2)

    def move(self):
        self.ride = True
        while self.ride:
            right_detect = int(self.right_sensor.value)
            if right_detect == 0:
                self.forward()
            else:
                self.try_to_find_line()
        time.sleep(0.3)


    def stop(self):
        self.ride = False
        self.right_motor.stop()
        self.left_motor.stop()
        
        #self.right_sensor.close()
        #self.left_sensor.close()

