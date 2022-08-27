import sqlite3
from sqlite3 import Error

import config
from services import location
from services.i2c import I2cTemperatureDeviceClient
from services.weather import WeatherTemperatureClient, WeatherTemperatureMockClient, WeatherTemperatureWebClient


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_measurement(conn, measurement):
    """
    Create a new measurement
    :param conn:
    :param measurement:
    :return:
    """

    sql = "INSERT INTO MEASUREMENTS(NAME,VALUE,TIMESTAMP) VALUES(?,?,?)"
    cur = conn.cursor()

    print(measurement)

    cur.execute(sql, tuple(measurement))
    conn.commit()

    return cur.lastrowid


def main():
    database = r"test.db"
    conn = create_connection(database)

    location.initialize_location_context()
    location_data = location.get_location_from(config.LOCATION_NAME)

    weather_web_client = WeatherTemperatureWebClient()
    weather_device_client: WeatherTemperatureClient

    if config.DEBUG:
        weather_device_client = WeatherTemperatureMockClient()
    else:
        weather_device_client = I2cTemperatureDeviceClient()

    weather_data = weather_web_client.get_current_temperature(latitude=location_data.latitude, longitude=location_data.longitude, api_key=config.WEATHER_API_KEY)
    device_data = weather_device_client.get_current_temperature()

    with conn:
        create_measurement(conn, weather_data)
        for device in device_data:
            create_measurement(conn, device)


if __name__ == '__main__':
    main()
