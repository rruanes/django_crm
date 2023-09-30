# Install MySQL on your computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'J@nSeVen12'
)

# Prepare a cursor object
cursor_object = database.cursor()

# Create a database
cursor_object.execute("CREATE DATABASE mysqldb")

print("All done!")