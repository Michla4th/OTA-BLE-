import ota
import time

ota_device = ota.OTA()

def setup():
    ota_device.send_data("Xin chào ESP32")

def loop():
    while True:
        time.sleep(10)

if __name__ == "__main__":
    try:
        setup()
        loop()
    except Exception as e:
        print(f"error: {e}")
        ota_device.send_data(f"error: {e}")
