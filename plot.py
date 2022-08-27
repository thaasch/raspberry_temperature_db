#!/usr/bin/python

import matplotlib.pyplot as plt
import pandas
import sqlite3

conn = sqlite3.connect('test.db')
sql = """select * from MEASUREMENTS"""

data = pandas.read_sql(sql, conn)
data.TIMESTAMP = pandas.to_datetime(data.TIMESTAMP)

data = data.set_index("TIMESTAMP").drop(columns="ID")

data = data.groupby([pandas.Grouper(freq='H'), 'NAME']).median().unstack()
data.columns = data.columns.get_level_values(1)

data.plot(kind='line')
plt.title("Temperaturen Vergleich")
plt.show()
