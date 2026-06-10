'''
Desk-mounted simracing handbrake firmware
Bowie 2026
Adafruit Human Interface Device
Seeed XIAO RP2040 on CircuitPython

hid_gamepad.py
gamepad driver
'''

import struct

class SimHandbrake:
    def __init__(self,devices): #initialise handbrake class
        self._device = None
        for dev in devices:
            if dev.usage_page == 0x01 and dev.usage == 0x05: #find HID with gamepad hex ids
                self._device = dev #set class device to found gamepad
                break
        if not self._device:
            raise RuntimeError("Gamepad HID not found.")

        def send_axis(self,value):
            #method to send handbrake actuation value, sends single signed bit (-127 to 127)
            report = struct.pack("<bxxx",value) #convert value into formatted bytes obj
            self._device.send_report(report)
            
        
