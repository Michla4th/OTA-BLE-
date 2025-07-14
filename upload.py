import time
import kulbot
import define

Rob = kulbot.KULBOT()

def my_new_handler(data):
    print("Dữ liệu mới:", data)

def setup(ble=None):
    ble.set_fallback_handler(my_new_handler)
    print("Begin")
    Rob.KULBOT_MOTORENCODER_INIT()
    
def loop():
    while True:
        # Rob.KULBOT_RGB_ALL_ON(0)
        # # Rob.KULBOT_MOTORENCODER_RUN1(0, 100, 0)
        # # Rob.KULBOT_SERVO_SET_ANGLE(1, 180)
        # time.sleep(1)
        # Rob.KULBOT_RGB_ALL_OFF()
        # # Rob.KULBOT_MOTORENCODER_RUN1(0, 100, 1)
        # # Rob.KULBOT_SERVO_SET_ANGLE(1, 0)
        time.sleep(1)
