from gpiozero import LED, Buzzer


class Signals:

    def __init__(self):
        self.led = LED(16)
        self.buzzer = Buzzer(21, active_high=False)

    def waiting_for_client(self, a):
        self.led.blink()
        self.buzzer.off()

    def client_connected(self, a):
        self.__led_controlled_mode__()

    def enabled_remote_controlled_mode(self):
        self.__led_controlled_mode__()

    def enabled_autnomous_mode(self):
        self.__led_autonomous_mode__()

    def __led_autonomous_mode__(self):
        self.led.blink(on_time=0.3, off_time=0.2)

    def __led_controlled_mode__(self):
        self.led.on()