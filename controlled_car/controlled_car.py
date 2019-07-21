from gpiozero import Motor

class ControlledCar:

    def __init__(self, left_motor = Motor(27, 22), right_motor =  Motor(26, 17), right_motor_correction_speed=1, left_motor_correction_speed=1):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.right_motor_correction_speed = right_motor_correction_speed
        self.left_motor_correction_speed = left_motor_correction_speed
        
    def __forward__(self, speed=1):
        self.right_motor.forward(self.right_motor_correction_speed * speed)
        self.left_motor.forward(self.left_motor_correction_speed * speed)

    def __backward__(self, speed=1):
        self.right_motor.backward(self.right_motor_correction_speed * speed)
        self.left_motor.backward(self.left_motor_correction_speed * speed)

    def __left__(self, speed=1):
        self.right_motor.forward(self.right_motor_correction_speed * speed)
        self.left_motor.backward(self.left_motor_correction_speed * speed)

    def __right__(self, speed=1):
        self.right_motor.backward(self.right_motor_correction_speed * speed)
        self.left_motor.forward(self.left_motor_correction_speed * speed)

    def move(self, position, forward_speed=1, backward_speed=1, left_speed=1, right_speed=1):
        if position.top:
            self.__forward__(forward_speed)
        elif position.bottom:
            self.__backward__(backward_speed)
        elif position.right:
            self.__right__(right_speed)
        elif position.left:
            self.__left__(left_speed)

    def stop(self, position):
        self.right_motor.stop()
        self.left_motor.stop()
