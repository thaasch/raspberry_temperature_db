import datetime
import smbus

import services.registers as registers
from services.dto import Measurement
from services.weather import WeatherTemperatureClient


class I2cTemperatureDeviceClient(WeatherTemperatureClient):
    def __int__(self):
        self.bus = smbus.SMBus(1)

    def get_current_temperature(self, **kwargs):
        return [Measurement(str(device), self._read_temperature(device), datetime.datetime.now()) for device in
                enumerate(registers.DEVICES) if
                self._configure_devices(registers.DEVICES, 12)]

    def _configure_devices(self, address, bit_resolution):
        assert (9 <= bit_resolution <= 12)
        config = self.bus.read_byte_data(address, registers.REG_CONFIG)
        config &= ~(0b11 << registers.SHIFT_ADC_RES)
        config |= ((int(bit_resolution) - 9) << registers.SHIFT_ADC_RES)
        self.bus.write_byte_data(address, registers.REG_CONFIG, config)

    def _read_register(self, address, register, length):
        data = self.bus.read_i2c_block_data(address, register, length)
        return data

    def _read_temperature(self, address):
        temperature = self._read_register(address, registers.REG_TEMP, 2)

        if len(temperature) < 2:
            return None
        return float((temperature[0] << 8) + temperature[1]) / (2 ** 8)
