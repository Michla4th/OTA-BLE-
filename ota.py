# import machine, bluetooth
# from ble import BLEUART
# import os
# import define
# import time

# class OTA:
#     def __init__(self):
#         self.uploading = False
#         self.ble = bluetooth.BLE()
#         self.uart = BLEUART(self.ble, name='kulbot-2')
#         self.uart.irq(handler=self.on_rx)

#     def on_rx(self):
#         """Handle incoming BLE data."""
#         data = self.uart.read().decode().rstrip()

#         # Command handling
#         if data == 'upload':
#             self.uart.write("Ready to upload code...\n")
#             self.uploading = True  

#             # Create a new upload.py file
#             with open("upload.py", "w") as file:
#                 file.write("")

#         elif data == 'done':
#             self.uploading = False
#             self.uart.write("Firmware updated! Restarting device...\n")
#             time.sleep(1) 
#             machine.reset()  # Reset the device after updating
#             # try:
#             #     exec(open("upload.py").read())
#             #     self.uart.write("Firmware updated! Restarting device...\n")
#             #     os.rename('upload.py', 'main.py')
#             #     time.sleep(1) 
#             #     machine.reset()  # Reset the device after updating
#             # except Exception as e:
#             #     print("error: ", e)
#             #     self.uart.write(e)

#         elif self.uploading:
#             try:
#                 # Write received data into the upload.py file
#                 with open("upload.py", "a") as file:
#                     file.write(data + "\n")
#                     self.uart.write('.')
#             except OSError as e:
#                 print(f"File write error: {e}")


import machine, bluetooth
from ble import BLEUART
import os
import time

def crc16_ccitt(data: bytes, crc: int = 0xFFFF) -> int:
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
            crc &= 0xFFFF
    return crc

class OTA:
    def __init__(self, fallback_handler=None):
        self.uploading = False
        self.expected_crc = None
        self.ble = bluetooth.BLE()
        self.uart = BLEUART(self.ble, name='kulbot-ota')
        self.uart.irq(handler=self.on_rx)
        self.fallback_handler = fallback_handler

    def set_fallback_handler(self, handler):
        """Change callback function."""
        self.fallback_handler = handler

    def send_data(self, data):
        """Send data over BLE."""
        if self.uart:
            self.uart.write(data + "\n")
        else:
            print("UART not initialized")

    def on_rx(self):
        """Handle incoming BLE data."""
        data = self.uart.read().decode().rstrip()

        if data == 'upload':
            self.uart.write("Ready to upload code...\n")
            self.uploading = True
            self.expected_crc = None
            with open("upload.py", "w") as file:
                file.write("")

        elif data.startswith("crc:"):
            try:
                self.expected_crc = int(data[4:], 16)
                self.uart.write("CRC received: %04X\n" % self.expected_crc)
            except ValueError:
                self.uart.write("Invalid CRC format!\n")

        elif data == 'done':
            self.uploading = False
            if self.expected_crc is None:
                self.uart.write("No CRC received. Upload aborted.\n")
                return

            try:
                with open("upload.py", "rb") as f:
                    file_data = f.read()
                actual_crc = crc16_ccitt(file_data)

                if actual_crc == self.expected_crc:
                    self.uart.write("CRC OK. Updating firmware...\n")
                    # os.rename("upload.py", "main.py")
                    time.sleep(1)
                    machine.reset()
                else:
                    self.uart.write("CRC mismatch! Upload failed.\n")
                    self.uart.write("Expected: %04X, Got: %04X\n" % (self.expected_crc, actual_crc))
            except Exception as e:
                self.uart.write("Error: %s\n" % str(e))

        elif self.uploading:
            try:
                with open("upload.py", "a") as file:
                    file.write(data + "\n")
                self.uart.write(".")  # progress feedback
            except OSError as e:
                print(f"File write error: {e}")
                self.uart.write("Write error\n")
        
        elif self.uploading == False and self.fallback_handler:
            self.fallback_handler(data)

