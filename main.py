from bluedot import BlueDot
from signal import pause
from car_warden import CarWarden
from signals import Signals

bd = BlueDot()
signals = Signals()
car_warden = CarWarden(signals)

def move(position):
    if bd.interaction.duration > 1.0 and position.middle:
        signals.buzzer.on()
    car_warden.move(position)
            
def stop(position):
    signals.buzzer.off()
    car_warden.stop(position)
    if bd.interaction.duration > 1.0 and position.middle:
        car_warden.change_car_control_type(position)

try:
    signals.waiting_for_client(0)

    bd.when_pressed = move
    bd.when_moved = move
    bd.when_released = stop
    bd.when_client_connects = signals.client_connected
    bd.when_client_disconnects = signals.waiting_for_client

    pause()

except KeyboardInterrupt:
    signals.led.off()
    signals.buzzer.off()