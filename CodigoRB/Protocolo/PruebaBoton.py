#Raspberry Pi Master
# -*- encoding: utf-8 -*-
import time
from smbus import SMBus

address = 0x08 #la dirección del bus
bus = SMBus(1) #indicado por la dirección /dev/ic2-1
time.sleep(1)

while True:
    data = bus.read_byte(address)
    
    if data == 0x01:
        print("Button pressed on ESP32")
    elif data == 0x10:
        print("Button not pressed on ESP32")
    #time.sleep(0.1)