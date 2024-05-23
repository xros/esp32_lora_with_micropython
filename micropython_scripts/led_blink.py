import machine
import time
pin37 = machine.Pin(37, machine.Pin.OUT)
print('lighting on and off LED')
pin37.value(1)
time.sleep(1)
pin37.value(0)
time.sleep(1)
pin37.value(1)
