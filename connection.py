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

# helper for executing queries
def executeQuery(query, parameters=()):
    connection, cursor = connect()
    cursor.execute(query, parameters)

    # SELECT queries
    if query.strip().upper().startswith("SELECT"):
        result = cursor.fetchall()

    # INSERT, UPDATE, DELETE queries
    else: 
        connection.commit()  
        result = None

    cursor.close()
    connection.close()

    return result
    
def login(query, parameters=()):

    result = executeQuery(query, parameters)
    #If result exists, email + pw combo exists
    if(result):
        return result[0]    
    return []
    
