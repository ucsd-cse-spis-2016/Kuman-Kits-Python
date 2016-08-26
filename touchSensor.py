import RPi.GPIO as GPIO
import time

#Set up the pins
sensor = 12
value = 0

#Standard board setup
def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(sensor, GPIO.IN)


def loop():
    while True:
        value = GPIO.input(sensor)
        print value

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
