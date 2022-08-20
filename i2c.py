#!/usr/bin/python

import smbus

bus = smbus.SMBus(1)

DEVICE_ADDRESS = 0x15      #7 bit address (will be left shifted to add the read write bit)
DEVICE_REG_MODE1 = 0x00
DEVICE_REG_LEDOUT0 = 0x1d

DEVICES = [0x40, 0x41, 0x42]

def get_values():
    for device in DEVICES:
        bus.read_i2c_block_data(device)