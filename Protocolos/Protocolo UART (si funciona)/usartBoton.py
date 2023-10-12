import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600)   # Serial port on Raspberry Pi

try:
    while True:
        if ser.in_waiting > 0:
            button_state = ser.read(1)
            print("Received Button State from STM32:", button_state)
        time.sleep(1)
except KeyboardInterrupt:
    ser.close()