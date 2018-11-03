from bluedot import BlueDot
from signal import pause
from car_warden import CarWarden
from control_type import ControlType
from signals import Signals

car_control_mode = ControlType.RemoteControlled

bd = BlueDot()
signals = Signals(car_control_mode)
car_warden = CarWarden(car_control_mode, signals)

try:
    signals.waiting_for_client()

    bd.when_pressed = car_warden.move
    bd.when_moved = car_warden.move
    bd.when_released = car_warden.stop
    bd.when_double_pressed = car_warden.change_car_control_type
    bd.when_client_connects = signals.client_connected
    bd.when_client_disconnects = signals.waiting_for_client

    pause()

except KeyboardInterrupt:
    signals.led.off()
    signals.buzzer.off()