import RPi.GPIO as GPIO

led = 13
temp = 3
value = 0

def setup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led, GPIO.OUT)
    GPIO.setup(temp, GPIO.IN)

def loop()
    value = GPIO.input(temp)

    if value == HIGH:
        GPIO.output(led, HIGH)

    else:
        GPIO.output(led, LOW)

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
      loop()
    except KeyboardInterrupt:  
      destroy()
