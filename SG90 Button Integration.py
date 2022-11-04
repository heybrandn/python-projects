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
x = 1

while True:
    while testTest:
        if button.value():
            print(x)
            if x == 1:
                test = True
                x = 0
                oled.fill(0)
                oled.text("Position 1", 40, 32)
                oled.show()
                for position in range(1000,9000,10):
                    pwm.duty_u16(position)
                    time.sleep(0.01)
            else:
                test = True
                x = 1
                oled.fill(0)
                oled.text("Position 0", 40, 32)
                oled.show()
                for position in range(9000,1000,-10):
                    pwm.duty_u16(position)
                    time.sleep(0.01)
