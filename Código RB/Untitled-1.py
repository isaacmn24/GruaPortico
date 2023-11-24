
bin_y= "0001"
Objetivo_Y = 2
cadena_bits_y = bin_y+format(bin(Objetivo_Y)[2:],f'0{"3"}')
cadena_enviar = cadena_bits_y.encode()

print(cadena_enviar)