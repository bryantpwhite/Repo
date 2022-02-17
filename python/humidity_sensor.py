import time
delay_time = 0.1 # time to delay between multiple measurements

# Set up "board" (QT Py 2040)
import board
import busio # contains an interface for using hardware-driven I2C communication from your board
i2c = busio.I2C(board.SCL1, board.SDA1)

# Use the following lines with the tiny 0.91" OLED display
oled_reset = board.D9

import displayio
displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)

import adafruit_displayio_ssd1306
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)
# Code to use the built-in boot button on the board. Pressed is False (grounded)
import digitalio
button = digitalio.DigitalInOut(board.BUTTON)
button.switch_to_input(pull=digitalio.Pull.UP)

# humidity/temperature sensor board
import adafruit_hts221
hts = adafruit_hts221.HTS221(i2c)

# Program will do nothing until the button is pressed.
while button.value: # button.value will be True when not pressed
    pass

# read the rel humidity and temp every second
if True:
    print() # this generates a newline to make up for the missing one at the end of the loop
    print() # this generates another newline to clear the text off the top of the display
    print("RH: %.2f %%" % hts.relative_humidity)
    print("Temp: %.2f C" % hts.temperature, end ="") # suppress newline to prevent text shifting up on display
    print("Temp: %.2f C" % hts.temperature) # use this line instead if not using tiny display
    time.sleep(delay_time)

print('done')
