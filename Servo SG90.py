from machine import Pin, PWM, I2C
import time
from ssd1306 import SSD1306_I2C
import framebuf
import random

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=200000)
oled = SSD1306_I2C(128, 64, i2c)   
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
oled.fill(0)
oled.show()

testTest = True
test = False

pwm = PWM(Pin(15))
pwm.freq(50)

MIN = 1000000
MAX = 3000000
while True:
    pwm.duty_ns(MIN)
    time.sleep(1)
    pwm.duty_ns(MAX)
    time.sleep(1)
