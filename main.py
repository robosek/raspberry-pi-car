from bluedot import BlueDot
from signal import pause
from car_warden import CarWarden
from control_type import ControlType
from signals import Signals

car_control_mode = ControlType.RemoteControlled

bd = BlueDot()
bd.rotation_segments = 2
signals = Signals(car_control_mode)
car_warden = CarWarden(car_control_mode, signals)

def move(position):
    car_warden.move(position)
    if bd.interaction.duration > 3.0 and position.middle:
        signals.buzzer.on()
            
def stop(position):
    car_warden.stop(position)
    if bd.interaction.duration > 3.0 and position.middle:
        car_warden.change_car_control_type(position)
    signals.buzzer.off()
    

try:
    signals.waiting_for_client("")

    bd.when_pressed = move
    bd.when_moved = move
    bd.when_released = stop
    bd.when_client_connects = signals.client_connected
    bd.when_client_disconnects = signals.waiting_for_client

    pause()

except KeyboardInterrupt:
    signals.led.off()
    signals.buzzer.off()