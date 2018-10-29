class ControlledCar:

    def __init__(self, car):
        self.car = car

    def __forward__(self, speed=1):
        self.car.right_motor.forward(self.car.right_motor_speed * speed)
        self.car.left_motor.forward(self.car.left_motor_speed * speed)

    def __backward__(self, speed=1):
        self.car.right_motor.backward(self.car.right_motor_speed * speed)
        self.car.left_motor.backward(self.car.left_motor_speed * speed)

    def __left__(self, speed=1):
        self.car.right_motor.forward(self.car.right_motor_speed * speed)
        self.car.left_motor.backward(self.car.left_motor_speed * speed)

    def __right__(self, speed=1):
        self.car.right_motor.backward(self.car.right_motor_speed * speed)
        self.car.left_motor.forward(self.car.left_motor_speed * speed)

    def stop(self):
        self.car.right_motor.stop()
        self.car.left_motor.stop()

    def move(self, position, forward_speed = 1, backward_speed = 1, left_speed = 1, right_speed = 1):
        if position.top:
            self.__forward__(forward_speed)
        elif position.bottom:
            self.__backward__(backward_speed)
        elif position.right:
            self.__right__(right_speed)
        elif position.left:
            self.__left__(left_speed)