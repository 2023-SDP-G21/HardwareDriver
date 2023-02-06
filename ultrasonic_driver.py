# Importing modules and classes
import time
from gpiozero import DigitalInputDevice, DigitalOutputDevice

# Defining sensor class
class UltraSonic:
  
    def __init__(self, echo, trigger):
        # Assingning ultrasonic sensor echo and trigger GPIO pins
        self._usoundecho = DigitalInputDevice(echo)
        self._usoundtrig = DigitalOutputDevice(trigger)
        # Assigning speed of sound (cm/s)
        self.speedofsound = 34300

    @property
    def distance(self):
        # Sending trigger pulse (~10 us)
        self._usoundtrig.on()
        time.sleep(0.000010)
        self._usoundtrig.off()
        # Detecting echo pulse start
        while self._usoundecho.value == 0:
            trise = time.perf_counter()
        # Detecting echo pulse end
        while self._usoundecho.value == 1:
            tfall = time.perf_counter()
        # Returning distance (cm)
        return 0.5 * (tfall-trise) * self.speedofsound

    @distance.setter
    def distance(self, _):
        print('"distance" is a read only attribute.')

    def __del__(self):
        self._usoundecho.close()
        self._usoundtrig.close()
