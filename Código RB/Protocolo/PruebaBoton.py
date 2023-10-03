#Raspberry Pi Master
# -*- encoding: utf-8 -*-
import time
from smbus import SMBus

address = 0x08 #la dirección del bus
bus = SMBus(1) #indicado por la dirección /dev/ic2-1
time.sleep(1)

while True: 
    button_state = bus.read_byte(address)
    print(button_state)
    if button_state == 1:
        print("Button pressed\n")
    else:
        print("Button not pressed\n")

    #time.sleep(0.1)