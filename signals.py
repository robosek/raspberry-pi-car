from gpiozero import LED, Buzzer
from control_type import ControlType


class Signals:

    def __init__(self, car_control_type):
        self.car_control_type = car_control_type
        self.led = LED(16)
        self.buzzer = Buzzer(21, active_high=False)

    def waiting_for_client(self):
        self.led.blink()

    def client_connected(self):
        self.__led_controlled_mode__() if self.car_control_mode == ControlType.RemoteControlled else self.__led_autonomous_mode__()

    def enable_remote_controlled_mode(self):
        self.__buzzer_switch_mode__()
        self.__led_controlled_mode__()

    def enable_autnomous_mode(self):
        self.__buzzer_switch_mode__()
        self.__led_autonomous_mode__()

    def __buzzer_switch_mode__(self):
        self.buzzer.blink(on_time=0.3, off_time=0.1, n=2)

    def __led_autonomous_mode__(self):
        self.led.blink(on_time=0.3, off_time=0.2)

    def __led_controlled_mode__(self):
        self.led.on()