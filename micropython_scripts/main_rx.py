from sx1268 import SX1268
import time
import ssd1306
from machine import SoftI2C, Pin

sx = SX1268(spi_bus=1, clk=5, mosi=6, miso=3, cs=7, irq=33, rst=8, gpio=34)

# LoRa
'''
sx.begin(freq=433, bw=500.0, sf=12, cr=8, syncWord=0x12,
         power=-5, currentLimit=60.0, preambleLength=8,
         implicit=False, implicitLen=0xFF,
         crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=1.7, useRegulatorLDO=False, blocking=True)
'''

sx.begin(freq=434.0, bw=125.0, sf=9, cr=7, syncWord=0x12, power=14, currentLimit=60.0,
         preambleLength=8, implicit=False, implicitLen=0xFF, crcOn=True, txIq=False, rxIq=False,
         tcxoVoltage=0, useRegulatorLDO=False, blocking=True)
# FSK
##sx.beginFSK(freq=923, br=48.0, freqDev=50.0, rxBw=156.2, power=-5, currentLimit=60.0,
##            preambleLength=16, dataShaping=0.5, syncWord=[0x2D, 0x01], syncBitsLength=16,
##            addrFilter=SX126X_GFSK_ADDRESS_FILT_OFF, addr=0x00, crcLength=2, crcInitial=0x1D0F, crcPolynomial=0x1021,
##            crcInverted=True, whiteningOn=True, whiteningInitial=0x0100,
##            fixedPacketLength=False, packetLength=0xFF, preambleDetectorLength=SX126X_GFSK_PREAMBLE_DETECT_16,
##            tcxoVoltage=1.6, useRegulatorLDO=False,
##            blocking=True)

i2c = SoftI2C(sda=Pin(18), scl=Pin(17))
display = ssd1306.SSD1306_I2C(128, 64, i2c)
display.contrast(255)  # bright


i=1
while True:
    msg = sx.recv(len=0, timeout_en=False, timeout_ms=0)
    log = f'[*] Msg received {i}'
    print(log)
    display.fill(0)
    display.text('[*] Msg received', 0, 0, 1)
    display.text('at 434.0Mhz', 40, 12, 1)
    display.text(str(i), 40, 24, 1)
    display.text(msg[0].decode('utf-8'), 0, 36, 1)
    display.show()# power on the display, pixels redrawn
    i=i+1
    time.sleep(1)