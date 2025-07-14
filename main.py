import ota
# import upload
import time

ota_device = ota.OTA()

# def main():
#     try:
#         upload.setup(ota_device)
#         upload.loop()
#     except Exception as e:
#         print(f"error: {e}")

def my_new_handler(data):
    ota_device.send_data(data)
    print("Dữ liệu mới:", data)

def setup():
    ota_device.set_fallback_handler(my_new_handler)
    ota_device.send_data("Begin")

def loop():
    while True:
        # ota_device.send_data("Xin chào từ upload.py")
        time.sleep(10)

if __name__ == "__main__":
    try:
        setup()
        loop()
    except Exception as e:
        print(f"error: {e}")
        ota_device.send_data(f"error: {e}")