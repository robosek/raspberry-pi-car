from control_type import ControlType
from controlled_car import ControlledCar
from line_follower_car import LineFollowerCar
from gpiozero import Motor

class CarWarden:

    # right_motor_speed = 0.87 #correction

    def __init__(self, car_control_mode, signals):
        right_motor = Motor(26, 17)
        left_motor = Motor(22, 27)
        self.car_control_mode = car_control_mode
        self.signals = signals
        self.controlled_car = ControlledCar(right_motor, left_motor)
        self.line_follower_car = LineFollowerCar(0.65, right_motor, left_motor)

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
