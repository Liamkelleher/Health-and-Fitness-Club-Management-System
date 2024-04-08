import psycopg2
from psycopg2 import sql

#------CONNECTION SETUP------#
#Set up database connection
def connect():
    connection = psycopg2.connect(
        #Replace the strings inbetween " " with your database information
        dbname = "Health-and-Fitness-Club-Management-System",
        user = "postgres",
        password = "liam872003",
        host = "localhost",
        port = "5432"
    )

    cursor = connection.cursor()

    return connection, cursor

