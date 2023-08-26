#Raspberry Pi Master
from smbus import SMBus

addr = 0x8 #la dirección del bus
bus = SMBus(1) #indicado por la dirección /dev/ic2-1

num = 1
direccion = 0 #Variable que se le designa el valor correspondiente
              #para enviar la dirección en la que debe moverse
while num == 1:
  
  if direccion == 1:
    bus.write_byte(addr, 0x0) #Mover a la DERECCHA
  
  elif direccion == 2:
    bus.write_byte(addr, 0x1) #Mover a la IZQUIERDA

  elif direccion == 3:
    bus.write_byte(addr, 0x2) #Mover AL FRENTE

  elif direccion == 4:
    bus.write_byte(addr, 0x3) #Mover hacia ATRAS

  else:
    num == 0 #Se rompe el ciclo si el valor de direccion no esta entre 1 a 4

#De igual forma se deben enviar la cantidad de pasos a realizar

#Se debe realizar otro while o case para la cantidad de pasos, aunque estos deben estar alternando
#por lo cual deberian ser funciones que se llaman cuando son necesarios, donde la primera funcion
#es para enviar la información de la direccion en la que se mueve la grua y de forma consecutiva
#se llama la siguiente funcion para enviar la cantidad de pasos a realizar, una vez llegado a la
#posicion esperada se vuelve a llamar las funciones para el siguiente movimiento.
