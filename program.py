import psycopg2
from psycopg2 import sql
import clubMember 
import trainer as tr
import admin as ad

#------CONNECTION SETUP------#
#Set up database connection
connection = psycopg2.connect(
    #Replace the strings inbetween " " with your database information
    dbname = "yourDatabaseName",
    user = "yourUsername",
    password = "yourPassword",
    host = "yourHost",
    port = "yourPort"
)

#Create cursor to run SQL queries
cursor = connection.cursor()

#-----MAIN FLOW-----#
while True:

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("1. Register new Club Member")
    print("2. Log in as Club Member")
    print("3. Log in as Trainer")
    print("4. Log in as Administrative Staff")
    print("5. Quit")
    
    operation = int(input("Please choose an operation: "))

    match(operation):

        case 1:
            registerNewMember()

        case 2: 
            clubMemberLogin()

        case 3:
            trainerLogin()

        case 4:
            adminLogin()

        case 5: 
            break

#Close cursor and connection
cursor.close()
connection.close()