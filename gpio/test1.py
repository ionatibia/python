import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida


def blink():
	GPIO.output(17,True)
	time.sleep(1)
	GPIO.output(17,False)
	time.sleep(1)
	GPIO.cleanup()
blink()
