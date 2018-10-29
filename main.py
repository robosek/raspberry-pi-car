from bluedot import BlueDot
from gpiozero import Motor, LED, Buzzer, LineSensor
from signal import pause
from car import Car
from controlled_car import ControlledCar
from line_follower_car import LineFollowerCar
from control_type import ControlType

#GPIO 27 - IN 1
#GPIO 22 - IN 2
#GPIO 26 - IN 3
#GPIO 17 - IN 4

right_motor = Motor(26, 17)
left_motor = Motor(22, 27)
led = LED(16)
buzzer = Buzzer(21, active_high=False)
left_sensor = LineSensor(15)
right_sensor = LineSensor(16)
bd = BlueDot()

car_control_mode = ControlType.RemoteControlled
right_motor_speed = 0.87 #correction

car = Car(left_motor, right_motor, right_motor_correction_speed= right_motor_speed)
controlled_car = ControlledCar(car)
line_follower_car = LineFollowerCar(car, left_sensor, right_sensor)

def change_car_control_type():
    global car_control_mode;

    if car_control_mode == ControlType.Autonomus:
        car_control_mode = ControlType.RemoteControlled
    else:
        car_control_mode = ControlType.Autonomus

try:
    led.blink()

    bd.when_pressed = controlled_car.move if car_control_mode == ControlType.RemoteControlled else line_follower_car.move
    bd.when_moved = controlled_car.move if car_control_mode == ControlType.RemoteControlled else line_follower_car.move
    bd.when_released = controlled_car.stop if car_control_mode == ControlType.RemoteControlled else line_follower_car.stop
    bd.when_swiped = change_car_control_type
    bd.when_client_connects = led.on
    bd.when_client_disconnects = led.blink

    pause()
except KeyboardInterrupt:
    led.off()