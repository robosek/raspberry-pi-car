from bluedot import BlueDot
from signal import pause
from signals import Signals
from controlled_car import ControlledCar
from video import Video
import sys

def main(runVideo=False):
    bd = BlueDot()
    signals = Signals()
    car = ControlledCar()

    try:
        signals.waiting_for_client(0)

        if runVideo:
            video = Video()
            video.start_streaming()
            
        bd.when_pressed = car.move
        bd.when_moved = car.move
        bd.when_released = car.stop
        bd.when_client_connects = signals.client_connected
        bd.when_client_disconnects = signals.waiting_for_client

        pause()

    except KeyboardInterrupt:
        signals.led.off()
        signals.buzzer.off()

if __name__== "__main__":
    if len(sys.argv) > 1:
        runVideo = sys.argv[1]
        main(runVideo)
    else:
        main()