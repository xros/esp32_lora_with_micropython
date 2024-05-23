from machine import Pin, I2C, SoftI2C
import ssd1306

# using default address 0x3C
i2c = SoftI2C(sda=Pin(18), scl=Pin(17))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.contrast(255)  # bright
display.text('Hello, World!', 0, 0, 1)
display.show()# power on the display, pixels redrawn