import spidev
import time
import RPi.GPIO as GPIO

# Use the GPIO pin you connected to SS on Raspberry Pi
ss_pin = 24  # Replace with the actual GPIO pin number

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(ss_pin, GPIO.OUT)

# Set up SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, Device 0 (adjust if needed)

def read_spi_data():
    GPIO.output(ss_pin, GPIO.LOW)  # Enable SPI communication
    adc_data = spi.xfer2([0x00])  # Send a dummy byte to read data
    GPIO.output(ss_pin, GPIO.HIGH)  # Disable SPI communication
    return adc_data

try:
    while True:
        button_state = read_spi_data()
        print("Received Button State from STM32:", button_state)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    spi.close()
