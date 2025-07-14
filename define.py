"""
The firmware is developed by 3S JSC.
@ Written by LeKha
"""

""" -------------------------------WIFI AP--------------------------------- """
KULBOT_NAME    = "KULBOT-OTA"
KULBOT_VERSION = "1.0.0"
BLE_DATA = ""
BLE_STATE = False

""" -------------------------------RGB LED--------------------------------- """
WS2812_WIRE = 8

""" -------------------------------Motor--------------------------------- """
PWM_FREQ         = 31000
PWM_RESOLUTION   = 10
DRIVE_MOTOR_FREQ = 1600

""" -------------------------------Servo--------------------------------- """
DRIVE_PWM_FREQ     = 60
PWM_MIN_DUTY_CYCLE = 600
PWM_MAX_DUTY_CYCLE = 2400

""" -------------------------------Sensor--------------------------------- """
DRIVE_SENSOR_ADDRESS = 0x70
DRIVE_SENSOR_FREQ = 100000

""" -------------------------------LCD--------------------------------- """
DRIVE_LCD_ADDRESS    = 0x27  # 3F
DRIVE_LCD_NUM_CELLS  = 2
DRIVE_LCD_NUM_COLUMN = 16

""" -------------------------------Line sensor--------------------------------- """
LINE_SENSOR_ADDRESS = 0x3E  # 3E
LINE_SENSOR_LEFT    = 0
LINE_SENSOR_RIGHT   = 1

""" -------------------------------Touch sensor--------------------------------- """
TOUCH_SENSOR_ADDRESS = 0x38

""" -------------------------------IR sensor--------------------------------- """
IR_SENSOR_ADDRESS = 0x39

""" -------------------------------DHT12 sensor--------------------------------- """

""" -------------------------------Sonar sensor--------------------------------- """
SONAR_SENSOR_ADDRESS     = 0x10
SONAR_SENSOR_CONFIG_READ = 0x01

""" -------------------------------trafic light--------------------------------- """
TRAFFIC_SENSOR_ADDRESS = 0x3A

""" -------------------------------button led--------------------------------- """
BUTTON_LED_ADDRESS = 0x3c

""" -------------------------------Gryro sensor--------------------------------- """
GRYRO_SENSOR_ADDRESS = 0x68

""" -------------------------------Color sensor--------------------------------- """
COLOR_SENSOR_ADDRESS = 0x29

""" -------------------------------volume sensor--------------------------------- """
VOLUME_SENSOR_ADDRESS = 0x48

""" -------------------------------soil hum sensor--------------------------------- """
SOIL_HUM_SENSOR_ADDRESS = 0x48

""" -------------------------------light sensor--------------------------------- """
LIGHT_SENSOR_ADDRESS = 0x48

""" -------------------------------Gas sensor--------------------------------- """
GAS_SENSOR_ADDRESS = 0x48

""" -------------------------------Joystick sensor--------------------------------- """
JOYSTICK_SENSOR_ADDRESS = 0x48

""" -------------------------------Camera AI (ESP32 Cam)--------------------------------- """


