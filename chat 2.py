import RPi.GPIO as GPIO
import time
import curses

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 8
pinMotorBBackwards = 7

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 30
DutyCycleB = 30
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Initialize curses for keyboard input
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

# Turn all motors off
def stopmotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

try:
    while True:
        char = stdscr.getch()
        if char == ord('q'):
            break
        elif char == ord('w'):
            # Move forward
            pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
            pwmMotorABackwards.ChangeDutyCycle(Stop)
            pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
            pwmMotorBBackwards.ChangeDutyCycle(Stop)
        elif char == ord('s'):
            # Move backward
            pwmMotorAForwards.ChangeDutyCycle(Stop)
            pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
            pwmMotorBForwards.ChangeDutyCycle(Stop)
            pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
        elif char == ord('a'):
            # Turn left
            pwmMotorAForwards.ChangeDutyCycle(Stop)
            pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
            pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
            pwmMotorBBackwards.ChangeDutyCycle(Stop)
        elif char == ord('d'):
            # Turn right
            pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
            pwmMotorABackwards.ChangeDutyCycle(Stop)
            pwmMotorBForwards.ChangeDutyCycle(Stop)
            pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
        elif char == ord('x'):
            # Stop motors
            stopmotors()

finally:
    curses.endwin()  # Restore terminal settings
    GPIO.cleanup()
