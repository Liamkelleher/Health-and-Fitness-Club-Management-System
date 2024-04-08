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

def initData():
    connection, cursor = connect()
    
    cursor.execute("""SELECT COUNT(*) FROM trainingEquipment""")

    if(cursor.fetchone()[0] == 0):
        cursor.execute(
            """INSERT INTO trainingEquipment (name, status) VALUES
            ('Bench', 'Good'),
            ('Squat rack', 'Decent'),
            ('Treadmill', 'Not functional');
            """)
        connection.commit()

    connection.close()
    cursor.close()

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
    