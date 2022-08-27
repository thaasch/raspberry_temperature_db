#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE MEASUREMENTS
         (ID INTEGER PRIMARY KEY,
         NAME           TEXT    NOT NULL,
         VALUE          FLOAT   NOT NULL,
         TIMESTAMP      DATE);''')
print("Table created successfully")

conn.close()
