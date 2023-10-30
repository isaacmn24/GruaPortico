import serial
#import time

ser = serial.Serial("/dev/ttyACM0", 115200)   # Serial port on Raspberry Pi

instrucciones = {
    "color"   : b'\x01',
    "distancia"   : b'\x02',
    "imanON"  : b'\x03',
    "imanOFF" : b'\x04',
    "motorXX" : b'\x05',
    "motorYY" : b'\x06'
    }

ins = str(input("Indique la instrucción: "))


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
    
        
    
    
    
    
    


