import dateutil.utils
from services import weather
import sqlite3
from sqlite3 import Error
from dto import measurement


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

    sql = "INSERT INTO MEASUREMENTS(ID, NAME,VALUE,TIMESTAMP) VALUES(?,?,?,?)"
    cur = conn.cursor()
    cur.execute(sql, measurement)
    conn.commit()

    return cur.lastrowid


def collect():
    data = []
    current_temperature = weather.get_current_temperature()
    entry = measurement(name='Outside', value=current_temperature, timestamp=dateutil.utils.today())
    data.append(entry)

    return data


def main():
    database = r"test.db"
    conn = create_connection(database)
    with conn:
        # Collect Data
        values = collect()

        # Write Data to DB
        create_measurement(conn, values)


if __name__ == '__main__':
    main()
