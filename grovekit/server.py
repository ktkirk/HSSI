from __future__ import print_function
import time
import socket
import Pyro4
import pyupm_grove as grove
import pyupm_servo as servo
import pyupm_th02 as th02
import pyupm_i2clcd as lcd
import pyupm_guvas12d as upmUV
import pyupm_biss0001 as upmMotion
import pyupm_rotaryencoder as upmRotaryEncoder
import pyupm_grovespeaker as upmGrovespeaker

class Server(object):
    def __init__(self):
        self.button = None
        self.encoder = None
        self.light = None
        self.relay = None
        self.speaker = None
        self.motion = None
        self.lcd = None
        # Create the Grove LED object using GPIO pin 13
        self.led = grove.GroveLed(13)
        self.servo = None
        # Create the temperature sensor object using I2C
        self.th = th02.TH02()
        self.uv_sensor = None

    def info(self):
        # Print the name
        return {'button': self.button.name(),
                'led': self.led.name(),
                'light': self.light.name()}

    @Pyro4.oneway
    def blink(self, number=10):
        # Turn the LED on and off number times, pausing one second
        # between transitions
        for i in range(0, number):
            self.led.on()
            time.sleep(0.5)
            self.led.off()
            time.sleep(0.5)

    def getProxyObject(self, obj):
        if not hasattr(obj, '_pyroId'):
            self._pyroDaemon.register(obj)
        print("{} -> {}".format(type(obj), obj._pyroId))
        return obj

    def getEncoder(self, pins=(2, 3)):
        if self.encoder is None:
            # Instantiate a Grove Rotary Encoder, using signal pins D2 and D3
            self.encoder = upmRotaryEncoder.RotaryEncoder(*pins)
        return self.getProxyObject(self.encoder)

    def writeLCD(self, msg):
        self.lcd.write(msg.encode('latin_1'))

    def getLCD(self):
        if self.lcd is None:
            # Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
            self.lcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
            #self.lcd.old_write = self.lcd.write
        return self.getProxyObject(self.lcd)

    def getLED(self):
        return self.getProxyObject(self.led)

    def isButton(self):
        return self.button.value() == 1

    def getButton(self, pin=0):
        if self.button is None:
            # Create the button object using GPIO pin 1
            self.button = grove.GroveButton(pin)
        return self.getProxyObject(self.button)

    def getLightSensor(self, pin=2):
        if self.light is None:
            # Create the light sensor object using AI2 pin 2
            self.light = grove.GroveLight(pin)
        return self.getProxyObject(self.light)

    def getMotion(self, pin=7):
        if self.motion is None:
            # Instantiate a Grove Motion sensor on GPIO pin D7
            self.motion = upmMotion.BISS0001(pin)
        return self.getProxyObject(self.motion)

    def getRelay(self, pin=5):
        if self.relay is None:
            # Create the relay switch object using GPIO pin 5 default
            self.relay = grove.GroveRelay(pin)
        return self.getProxyObject(self.relay)

    def getSpeaker(self, pin=4):
        if self.speaker is None:
            # Instantiate a Grove Speaker on digital pin D4
            self.speaker = upmGrovespeaker.GroveSpeaker(pin)
        return self.getProxyObject(self.speaker)

    def getServo(self, pin=6):
        if self.servo is None:
            # Create the servo object using D6
            self.servo = servo.ES08A(pin)
        return self.getProxyObject(self.servo)

    def getUV(self, pin=3):
        if self.uv_sensor is None:
            # Instantiate a UV sensor on analog pin A3
            self.uv_sensor = upmUV.GUVAS12D(pin)
        return self.getProxyObject(self.uv_sensor)

    def getTemperature(self, unit='F'):
        """
        :param unit: string
        :return: float
        """
        celsius = self.th.getTemperature()
        c = unit.upper().encode('latin_1')[0]
        if c == 'F':
            return celsius * 9.0 / 5.0 + 32.0  # fahrenheit
        else:
            return celsius

    def getHumidity(self):
        return self.th.getHumidity()


def main():
    server = Server()
    hostname = socket.gethostname()
    Pyro4.config.HOST = "{}.local".format(hostname)
    Pyro4.config.ONEWAY_THREADED = True
    Pyro4.Daemon.serveSimple(
        {
            server: "edison.iot.server"
        },
        ns=True)


if __name__ == "__main__":
    main()