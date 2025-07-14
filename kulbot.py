"""
The firmware is developed by 3S JSC.
@ Written by Engineer LeKha
"""

from machine import SoftI2C, Pin, PWM
from neopixel import NeoPixel
import uasyncio as asyncio

import pca9685
from time import sleep
from define import *
from pin import *

class KULBOT:
    def __init__(self):
        self._RGB_WS2812 = NeoPixel(Pin(WS1812_PIN), WS2812_WIRE)
        self._BUZZER_PIN = Pin(BUZZER_PIN, Pin.OUT)
        self._BUZZER_PIN.off()
        self.KULBOT_RGB_ALL_OFF()

    #========================== LED MODULE ==========================#
    def KULBOT_RGB_ON(self, led, color):
        if color == 0:   self._RGB_WS2812[led] = (255, 0, 0)     # red
        elif color == 1: self._RGB_WS2812[led] = (255, 100, 0)   # org
        elif color == 2: self._RGB_WS2812[led] = (255, 255, 0)   # yellow
        elif color == 3: self._RGB_WS2812[led] = (0, 255, 0)     # green
        elif color == 4: self._RGB_WS2812[led] = (0, 0, 255)     # blue
        elif color == 5: self._RGB_WS2812[led] = (0, 255, 255)   # cyan
        elif color == 6: self._RGB_WS2812[led] = (143, 0, 255)   # violet
        elif color == 7: self._RGB_WS2812[led] = (255, 255, 255) # white
        self._RGB_WS2812.write()

    def KULBOT_RGB_OFF(self, led):
        self._RGB_WS2812[led] = (0, 0, 0)
        self._RGB_WS2812.write()

    def KULBOT_RGB_ALL_ON(self, color):
        for i in range(8):
            self.KULBOT_RGB_ON(i, color)

    def KULBOT_RGB_ALL_OFF(self):
        for i in range(8):
            self._RGB_WS2812[i] = (0, 0, 0)
        self._RGB_WS2812.write()

    #========================== MOTOR MODULE ==========================#
    def KULBOT_MOTORENCODER_INIT(self):
        # Motor DC
        self.DC_MOTORS = ((8, 3, 4), (13, 5, 6))
        self.DRIVER_MOTOR = SoftI2C(sda=Pin(DRIVE_MOTOR_SDA), scl=Pin(DRIVE_MOTOR_SCL))
        self.LED_PWM_CHANEL1 = PWM(Pin(DRIVE_PWMA), freq=PWM_FREQ, duty=PWM_RESOLUTION)
        self.LED_PWM_CHANEL2 = PWM(Pin(DRIVE_PWMB), freq=PWM_FREQ, duty=PWM_RESOLUTION)
        # Servo
        self.DRIVE_PWM_SERVO = pca9685.PCA9685(i2c=self.DRIVER_MOTOR)
        self.DRIVE_PWM_SERVO.freq(DRIVE_PWM_FREQ)
        self.min_duty = self._us2duty(PWM_MIN_DUTY_CYCLE)
        self.max_duty = self._us2duty(PWM_MAX_DUTY_CYCLE)

    def _us2duty(self, value):
        return int(4095 * value / (1000000 / DRIVE_PWM_FREQ))
    
    def map(self, x, in_min, in_max, out_min, out_max):
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
    def _pin(self, pin, value=None):
        if value is None:
            return bool(self.DRIVE_PWM_SERVO.pwm(pin)[0])
        self.DRIVE_PWM_SERVO.pwm(pin, 4096 if value else 0, 0)

    def speed(self, index, value=None):
        pwm, in2, in1 = self.DC_MOTORS[index]
        if value > 0:
            self._pin(in2, False)
            self._pin(in1, True)
        elif value < 0:
            self._pin(in1, False)
            self._pin(in2, True)
        else:
            self._pin(in1, in2, False)

    def KULBOT_MOTORENCODER_RUN1(self, motor, speed, direction):
        self.speed(motor, 1 if direction == 0 else -1)
        duty = self.map(speed, 0, 100, 0, 1023)
        [self.LED_PWM_CHANEL1, self.LED_PWM_CHANEL2][motor].duty(duty)

    def position(self, index, degrees=None):
        duty = self.min_duty + (self.max_duty - self.min_duty) * max(0, min(180, degrees)) / 180
        self.DRIVE_PWM_SERVO.duty(index, min(self.max_duty, max(self.min_duty, int(duty))))

    def KULBOT_SERVO_SET_ANGLE(self, servo, ang):
        self.position(self._selection_servo_port(servo), ang)

    def _selection_servo_port(self, _port_servo):
        return 7 + _port_servo if 1 <= _port_servo <= 8 else None
    