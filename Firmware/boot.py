'''
Desk-mounted simracing handbrake firmware
Bowie 2026
Adafruit Human Interface Device
Seeed XIAO RP2040 on CircuitPython

boot.py
circuitpy boot init
'''
import usb_hid

usb_hid.enable((
    usb_hid.Device.GAMEPAD,
    ))
