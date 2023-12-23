# PIzero

import RPi.GPIO as GPIO
import time
import sys, termios, tty, os

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# Set up GPIO pins for motor control
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors backwards
def Backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Left():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

def Right():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

PIN_LED = 25
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.output(PIN_LED, 0)
button_delay = 0.2

for x in range(0, 3):
    GPIO.output(PIN_LED, 1)
    time.sleep(0.25)
    GPIO.output(PIN_LED, 0)
    time.sleep(0.25)

try:
    print("Press arrow keys to control the car. Press 'q' to quit.")
    while True:
        char = getch()
        
        if char == "q":
            StopMotors()
            break

        if char == "w":
            print('Up pressed')
            Forwards()
            time.sleep(button_delay)

        elif char == "s":
            print('Down pressed')
            Backwards()
            time.sleep(button_delay)

        elif char == "a":
            print('Left pressed')
            Left()
            time.sleep(button_delay)

        elif char == "d":
            print('Right pressed')
            Right()
            time.sleep(button_delay)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
