from machine import Pin
import time

print("\nKulbot firmware v1.0.0" + " on 1-1-2025; Developed by LeKha")
print('Type "help()" for more information.')

def _toggleLED(pin):
    CONTROL_POWER.off()

CONTROL_POWER = Pin(15, Pin.OUT)
CONTROL_POWER.on()
time.sleep(2)
INPUT_BUTTON_POWER = Pin(4, Pin.IN)
INPUT_BUTTON_POWER.irq(trigger=Pin.IRQ_RISING, handler=_toggleLED)

