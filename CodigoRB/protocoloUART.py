import serial
#import time

ser = serial.Serial("/dev/ttyACM0", 2000000)   # Serial port on Raspberry Pi

instrucciones = {
    "color"   : b'\x01',
    "imanON"  : b'\x02',
    "imanOFF" : b'\x03',
    "motorXX" : b'\x04',
    "motorYY" : b'\x05'
    }

def recibirUART(instruccion):
    transmitirUART(instruccion)
    if instruccion == "color":
        rgb = []
        while True:
            if ser.in_waiting > 0:
                rgb.append(ser.read(1))
                if ser.in_waiting <= 0:
                    return rgb
                
        
    
def transmitirUART(instruccion):
    ser.write(instrucciones[instruccion])
    
        
    
    
    
    
    


