from bluedot import BlueDot
from gpiozero import Robot, Motor
from signal import pause
from gpiozero import LED

#GPIO 27 - IN 1
#GPIO 17 - IN 4
#GPIO 22 - IN 2
#GPIO 26 - IN 3
 
rightMotor = Motor(26,17)
leftMotor = Motor(22,27)
led = LED(16)
bd = BlueDot()
rightMotorSpeed = 0.87 #correction

def forward(speed=1):
    rightMotor.forward(rightMotorSpeed * speed)
    leftMotor.forward(speed)
def backward(speed=1):
    rightMotor.backward(rightMotorSpeed*speed)
    leftMotor.backward(speed)
def left(speed=1):
    rightMotor.forward(speed)
    leftMotor.backward(speed)
def right(speed=1):
    leftMotor.forward(speed)
    rightMotor.backward(speed)
def stop():
    rightMotor.stop()
    leftMotor.stop()

try:
    led.blink()

    def move(pos):
        if pos.top:
            forward()
        elif pos.bottom:
            backward()
        elif pos.right:
            right(0.4)
        elif pos.left:
            left(0.4)

    bd.when_pressed = move
    bd.when_moved = move
    bd.when_released = stop
    bd.when_client_connects = led.on
    bd.when_client_disconnects = led.blink
    
    pause()

except KeyboardInterrupt:
    led.off(