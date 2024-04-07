import psycopg2
from psycopg2 import sql

#------CONNECTION SETUP------#
#Set up database connection
def connect():
    connection = psycopg2.connect(
        #Replace the strings inbetween " " with your database information
        dbname = "yourDatabaseName",
        user = "yourUsername",
        password = "yourPassword",
        host = "yourHost",
        port = "yourPort"
    )

    cursor = connection.cursor()

    return connection, cursor

