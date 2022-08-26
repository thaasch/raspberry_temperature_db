import smbus

bus = smbus.SMBus(1)

DEVICES = [0x40, 0x41, 0x42]


def get_values():
    for device in enumerate(DEVICES):
        bus.read_i2c_block_data(device)
