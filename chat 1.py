import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes

# Set up GPIO pins for motor control
left_motor = 17  # Adjust pin numbers as per your hardware configuration
right_motor = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_motor, GPIO.OUT)
GPIO.setup(right_motor, GPIO.OUT)

# Initialize the keyboard input device
dev = InputDevice('/dev/input/event0')  # Use the correct event device for your keyboard

# Define motor control functions
def forward():
    GPIO.output(left_motor, GPIO.HIGH)
    GPIO.output(right_motor, GPIO.HIGH)

def backward():
    GPIO.output(left_motor, GPIO.LOW)
    GPIO.output(right_motor, GPIO.LOW)

def stop():
    GPIO.output(left_motor, GPIO.LOW)
    GPIO.output(right_motor, GPIO.LOW)

try:
    print("Press arrow keys to control the car. Press 'q' to quit.")
    for event in dev.read_loop():
        if event.type == ecodes.EV_KEY:
            key_event = categorize(event)
            if key_event.keystate == key_event.key_down:
                if key_event.keycode == 'KEY_UP':
                    forward()
                elif key_event.keycode == 'KEY_DOWN':
                    backward()
            elif key_event.keystate == key_event.key_up:
                if key_event.keycode == 'KEY_UP' or key_event.keycode == 'KEY_DOWN':
                    stop()
                elif key_event.keycode == 'KEY_Q':
                    break

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
