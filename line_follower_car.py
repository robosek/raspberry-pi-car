from gpiozero import LineSensor
from car import Car
import time
from signal import pause

class LineFollowerCar(Car):

    def __init__(self, left_motor, right_motor, speed = 1,right_motor_correction_speed=1, left_motor_correction_speed=1):
        super().__init__(left_motor, right_motor, right_motor_correction_speed, left_motor_correction_speed)
        self.right_sensor = LineSensor(24, threshold=0.9)
        self.speed = speed
        
    def try_to_find_line(self):
        print("Try find line")
        self.stop()
        self.backward()
        time.sleep(0.3)
        self.left()
        time.sleep(0.3)
        self.right()

    
    def forward(self):
        print("Forward")
        self.right_motor.forward(self.right_motor_correction_speed * self.speed)
        self.left_motor.forward(self.speed)
    
    def backward(self):
        self.right_motor.backward(self.right_motor_correction_speed * self.speed)
        self.left_motor.backward(self.speed)
    def left(self):
        print(self.speed)
        self.right_motor.forward(self.speed)
        self.left_motor.backward(self.speed)
    def right(self):
        self.right_motor.forward(self.speed)
        self.left_motor.backward(self.speed)

    def move(self):
        self.ride = True
        while self.ride:
            right_detect = int(self.right_sensor.value)
            print(right_detect)
            if right_detect  == 0:
                self.forward()
            else:
                self.try_to_find_line()


    def stop(self):
        self.right_motor.stop()
        self.left_motor.stop()
        self.ride = False
        #self.right_sensor.close()
        #self.left_sensor.close()
    

    
