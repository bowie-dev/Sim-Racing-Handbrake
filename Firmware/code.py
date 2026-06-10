'''
Desk-mounted simracing handbrake firmware
Bowie 2026
Adafruit Human Interface Device
Seeed XIAO RP2040 on CircuitPython

code.py
main program file
'''
import time, board, analogio, usb_hid
from hid_gamepad import SimHandbrake

handbrake = SimHandbrake(usb_hid.devices)
sensor = analogio.AnalogIn(board.A0) #RP2040 pin A0 for KY-035 input

print('Calibrating, do not touch or actuate handbrake.')
time.sleep(1)

zero=sensor.value

#input value will either be 0-128, or 129-255 depending on magnet polarity.
#input raw scaled to 16bit therefore 0-32,896 or 33,153-65,535 (looks like theres missing zone between 328... and 331... but its impossible for these values to be measured-
#when circuitpy scales the 8bit to 16bit those values are jumped, its kinda 'faking' having high resolution (257x)

#lets say for example the handbrake zeroes around ~33k. as it is pulled down, assuming the magnet is aligned correctly, the raw value will increase. up to theoretically 65535
#we can parse this input by subtracting the read value from the zero, then dividing by a TUNED max value which should be around 33k (THIS WILL HAVE TO BE TWEAKED)
#this will give a float that represents between 0 and 1 of the handbrakes travel which can then be converted to a -127 to 127 value for the HID controller

minvalue=0 #placeholder values for now until ive build and assembled, 
maxvalue=33000 #input value 0-255 is scaled to 16bit (0-~65k) by circuitpython so est max value around 40k i guess
polarity=1 #this allows the polarity of the magnet to be changed via software if (i) someone accidentally press fits the magnet in incorrectly
deadzone=0.1 #allows for deadzone, 0.1 is 10%, 0.5 is 50%. This shouldn't be nessecary as most simulators have settings for axis deadzones but ill add it in bc its three lines.
frequency=100 #measured in Hz, polling rate for measurements. freq=0 or none means no waiting (probably not a good idea idk ill check)
print(f'Value zeroed at {zero}')

while True:
    raw = sensor.value #grab current raw value

    diff = raw-zero #compare to zero value

    travel = diff*polarity #flip if nessecary

    if travel<minvalue: #clip value to min and max
        travel=minvalue

    if travel>maxvalue:
        travel=maxvalue

    percentage=travel/maxvalue #calculate percentage travel

    if percentage < deadzone:
        percentage=0

    hidout = int((254 * percentage) - 127) # transforms 0 to 1 into -127 to 127

    handbrake.send_axis(hidout)

    if frequency and frequency!=0:
        time.sleep(1/frequency) #period = 1/frequency

    

    



