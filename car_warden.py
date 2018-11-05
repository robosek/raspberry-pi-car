from control_type import ControlType
from controlled_car import ControlledCar
from line_follower_car import LineFollowerCar
from gpiozero import Motor

class CarWarden:

    # right_motor_speed = 0.87 #correction

    def __init__(self, car_control_mode, signals):
        right_motor = Motor(26, 17)
        left_motor = Motor(27, 22)
        self.car_control_mode = car_control_mode
        self.signals = signals
        self.controlled_car = ControlledCar(left_motor,right_motor,right_motor_correction_speed=0.9)
        self.line_follower_car = LineFollowerCar(left_motor,right_motor,speed=0.3,right_motor_correction_speed=0.9)

    def move(self, position):
        if self.car_control_mode == ControlType.RemoteControlled:
            self.controlled_car.move(position)
        else:
            self.line_follower_car.move()

    def stop(self, position):
        if self.car_control_mode == ControlType.RemoteControlled:
            self.controlled_car.stop()

    def change_car_control_type(self, position):
        if self.car_control_mode == ControlType.Autonomous:
            self.car_control_mode = ControlType.RemoteControlled
            self.line_follower_car.stop()
            self.signals.enable_remote_controlled_mode()
        else:
            self.car_control_mode = ControlType.Autonomous
            self.signals.enable_autnomous_mode()
