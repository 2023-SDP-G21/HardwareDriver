import RPi.GPIO as GPIO
import time

class LED:
    
    def __init__(self, pin):
        self.pin = pin
        #initialise pin
        GPIO.setup(pin, GPIO.OUT)
        #set pin to high to turn off LED
        GPIO.output(pin, GPIO.HIGH)
        
        
    def __del__(self):
        self.pin.close()
        
    def on(self):
        GPIO.output(self.pin, GPIO.LOW)
        
    def off(self):
        GPIO.output(self.pin, GPIO.HIGH)
    
    
red = LED(17)
green = LED(27)
blue = LED(22)

while True:
# turn all on
    red.on()
    green.on()
    blue.on()
    time.sleep(2)
# turn all off
    red.off()
    green.off()
    blue.off()
    time.sleep(2)


        
        
    
