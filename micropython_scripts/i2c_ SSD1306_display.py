from machine import Pin, I2C
import ssd1306
# using default address 0x3C
i2c = I2C(sda=Pin(18), scl=Pin(17))
display = ssd1306.SSD1306_I2C(128, 64, i2c)