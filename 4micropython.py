# MicroPython code for Task 4

import dht
from machine import Pin
import time
import os


sensor = dht.DHT11(Pin(4))  # DHT11 data pin connected to GPIO4
filename = "dht_data.csv"


# Write header if file doesn’t exist
if filename not in os.listdir():
    with open(filename, "w") as f:
        f.write("Time,Temperature,Humidity\n")



while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Log data to CSV file
        with open(filename, "a") as f:
            f.write(f"{timestamp},{temp},{hum}\n")

        print(f"Logged: {timestamp}, Temp: {temp}°C, Humidity: {hum}%")
        time.sleep(5)

    except OSError as e:
        print("Sensor read error:", e)
