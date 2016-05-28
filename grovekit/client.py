from __future__ import print_function
import sys
import time
import Pyro4
import Pyro4.util
from random import randint


sys.excepthook = Pyro4.util.excepthook


def test_servo(servo):
    for i in range(10):
        # Set the servo arm to 0 degrees
        servo.setAngle(0)
        print('Set angle to 0')
        time.sleep(1)

        # Set the servo arm to 90 degrees
        servo.setAngle(90)
        print('Set angle to 90')
        time.sleep(1)

        # Set the servo arm to 180 degrees
        servo.setAngle(180)
        print('Set angle to 180')
        time.sleep(1)


def test_relay(relay):
    for i in range(3):
        relay.on()
        if relay.isOn():
            print(relay.name() + ' is on')
        time.sleep(1)
        relay.off()
        if relay.isOff():
            print(relay.name() + ' is off')
        time.sleep(1)


def main():
    Pyro4.config.HOST = '0.0.0.0'
    iot = Pyro4.Proxy("PYRONAME:edison.iot.server")
    #print(iot.info())
    iot.blink(10)

    lcd = iot.getLCD()
    speaker = iot.getSpeaker()
    # Play all 7 of the lowest notes
    speaker.playAll()

    light = iot.getLightSensor()
    button = iot.getButton()
    motion = iot.getMotion()
    encoder = iot.getEncoder()

    uv_sensor = iot.getUV()
    # analog voltage, usually 3.3 or 5.0 for UV sensor
    GUVAS12D_AREF = 5.0
    SAMPLES_PER_QUERY = 1024

    # The temperature sensor using I2C
    fahrenheit = iot.getTemperature('F')
    celsius = iot.getTemperature('C')
    humid = iot.getHumidity()
    print("{} degrees Celsius, or {} degrees Fahrenheit".format(celsius, fahrenheit))
    print("Humidity is {}%".format(humid))

    # Read the input and print, waiting one second between readings
    for i in range(20):
        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        lcd.setColor(r, g, b)
        lcd.setCursor(0, 0)
        #lcd.write('Hello World'.encode('latin_1'))
        iot.writeLCD('Hello World')
        lcd.setCursor(1, 0)
        #lcd.write("R:{} G:{} B:{}".format(r, g, b).encode('latin_1'))
        iot.writeLCD("R:{} G:{} B:{}".format(r, g, b))

        print("{} raw value is {}".format(light.name(), light.raw_value()), end='')
        print(", which is roughly {} lux".format(light.value()))
        print("AREF:  {0}, Voltage value (higher means more UV): {1}".format(
            GUVAS12D_AREF, uv_sensor.value(GUVAS12D_AREF, SAMPLES_PER_QUERY)))
        print("Position: {0}".format(encoder.position()))

        print("{} value is {}".format(button.name(), button.value()))
        if button.value():
            # Play a medium C-sharp
            speaker.playSound('c', True, "med")

        if motion.value():
            print("Detecting moving object")
        else:
            print("No moving objects detected")

        time.sleep(0.5)

    #test_relay(iot.getRelay())
    #test_servo(iot.getServo)

if __name__ == "__main__":
    main()