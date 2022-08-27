import smbus

bus = smbus.SMBus(1)

DEVICES = [0x40, 0x41, 0x42]
CMD = 0x34

REG_TEMP = 0x00
REG_CONFIG = 0x01
REG_HYSTERESIS = 0x02
REG_LIMIT = 0x03

SHIFT_ONE_SHOT = 7
SHIFT_ADC_RES = 5
SHIFT_FAULT_QUEUE = 3
SHIFT_ALERT_POLARITY = 2
SHIFT_COMP_INTR = 1
SHIFT_SHUTDOWN = 0


def configure_device(address, bit_resolution):
    assert (9 <= bit_resolution <= 12)
    config = bus.read_byte_data(address, REG_CONFIG)
    config &= ~(0b11 << SHIFT_ADC_RES)
    config |= ((int(bit_resolution) - 9) << SHIFT_ADC_RES)
    bus.write_byte_data(address, REG_CONFIG, config)


def read_register(address, register, length):
    data = bus.read_i2c_block_data(address, register, length)

    return data


def read_temperature(address):
    temperature = read_register(address, 0x00, 2)
    if len(temperature) < 2:
        return None
    return float((temperature[0] << 8) + temperature[1]) / (2 ** 8)


def get_values():
    values = []
    for device in enumerate(DEVICES):
        configure_device(device, 12)
        values.append({device: read_temperature(device)})

    return values
