from machine import Pin
import time

gpio_pin = Pin(16, Pin.OUT)


def pulse(pin, high_time, low_time):
    gpio_pin.value(1)
    time.sleep(high_time)

    gpio_pin.value(0)
    time.sleep(high_time)

    gpio_pin.value(1)
    time.sleep(high_time)

    gpio_pin.value(0)
    time.sleep(high_time)

    gpio_pin.value(1)
    time.sleep(high_time)

    gpio_pin.value(0)
    time.sleep(high_time)

    gpio_pin.value(1)
    time.sleep(high_time)

    gpio_pin.value(0)
    time.sleep(high_time)

    gpio_pin.value(1)
    time.sleep(low_time)

while True:
    pulse(gpio_pin, 0.2, 3)