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

#Add initial data if not included
def initData():
    query = """SELECT COUNT(*) FROM ClubMember"""
    result = executeQuery(query)

    if(result[0][0] == 0):
        query = """INSERT INTO ClubMember (email, password, fname, lname) VALUES
                ('bob@cm.com', 'bob', 'Bob', 'Z'),
                ('bobby@cm.com', 'bobby', 'Bobby', 'Z')
                """
        executeQuery(query)

    query = """SELECT COUNT(*) FROM trainer"""
    result = executeQuery(query)

    if(result[0][0] == 0):
        query = """INSERT INTO trainer (email, password, fname, lname) VALUES
                ('liamkelleher@trainer.com', 'liam', 'Liam', 'Kelleher'),
                ('lilyczarnecki@trainer.com', 'lily', 'Lily', 'Czarnecki'),
                ('hughhang@trainer.com', 'hugh', 'Hugh', 'Hang')
                """
        executeQuery(query)

    query = """SELECT COUNT(*) FROM admin"""
    result = executeQuery(query)

    if(result[0][0] == 0):
        query = """INSERT INTO admin (email, password, fname, lname) VALUES
                ('admin1@admin.com', 'admin1', 'Admin', '1'),
                ('admin2@admin.com', 'admin2', 'Admin', '2'),
                ('admin3@admin.com', 'admin3', 'Admin', '3')
                """
        executeQuery(query)

    #Training equipment check
    #Check if data is in table
    query = """SELECT COUNT(*) FROM trainingEquipment"""
    result = executeQuery(query)

    #Add data
    if(result[0][0] == 0):
        query = """INSERT INTO trainingEquipment (name, status) VALUES
            ('Bench', 'Good'),
            ('Squat rack', 'Decent'),
            ('Treadmill', 'Not functional');
            """
        executeQuery(query)

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
    
