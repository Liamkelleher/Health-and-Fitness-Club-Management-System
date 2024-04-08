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
    