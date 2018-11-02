from control_type import ControlType
from controlled_car import ControlledCar
from line_follower_car import LineFollowerCar
from signals import Signals


class CarWarden:

    # right_motor_speed = 0.87 #correction

    def __init__(self, car_control_mode):
        self.car_control_mode = car_control_mode
        self.signals = Signals(car_control_mode)
        self.controlled_car = ControlledCar()
        self.line_follower_car = LineFollowerCar(speed=0.65)

    def move(self, position):
        if self.car_control_mode == ControlType.RemoteControlled:
            self.controlled_car.move(position)
        else:
            self.line_follower_car.move()

    def stop(self):
        if self.car_control_mode == ControlType.RemoteControlled:
            self.controlled_car.stop()
        else:
            self.line_follower_car.stop()

    def change_car_control_type(self):
        if self.car_control_mode == ControlType.Autonomous:
            self.car_control_mode = ControlType.RemoteControlled
            self.signals.enable_remote_controlled_mode()
        else:
            self.car_control_mode = ControlType.Autonomous
            self.signals.enable_autnomous_mode()
