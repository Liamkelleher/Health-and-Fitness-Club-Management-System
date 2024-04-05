import psycopg2
from psycopg2 import sql

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


#-----FUNCTIONS-----#

#Add new Club Member
def registerNewMember():
    return

#-----MEMBER FUNTIONS-----#

def updateInfo(id):
    return

def updateAchievements(id):
    return

def updateStats(id):
    return

def displayDashboard(id):
    return

def scheduleTraining():
    return

def rescheduleTraining():
    return

def cancelTraining():
    return

def participateInClass():
    return

#Log in as Club Member
def clubMemberLogin():

    #Login using ID
    #If failed return
        #return  

    #If success
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("1. Update person information")
        print("2. Update fitness achievements")
        print("3. Update health statistics\n")
        print("4. Display dashboard\n")
        print("5. Schedule personal training session")
        print("6. Reschedule personal training session")
        print("7. Cancel personal training session")
        print("8. Participate in class")
        print("9. Logout")
        operation = int(input("Please choose an operation: "))

        match(operation):

            case 1:
                updateInfo()

            case 2:
                updateAchievements()

            case 3:
                updateStats()
                  
            case 4:
                displayDashboard()

            case 5:
                scheduleTraining()

            case 6:
                rescheduleTraining()

            case 7:
                cancelTraining()

            case 8:
                participateInClass()
                  
            case 9: 
                break


#-----TRAINER FUNTIONS-----#

def viewAvailibity():
    return

def addAvailability():
    return

def removeAvailability():
    return

def viewMember():
    return

#Log in as Trainer
def trainerLogin():

    #Login using ID
        #If failed return
        #return

    #If success
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("1. View availabity")
        print("2. Add availability")
        print("3. Remove availability")
        print("4. View member")
        print("5. Log out")

        operation = int(input("Please choose an operation"))

        match(operation):
            case 1:
                viewAvailibity()
                
            case 2:
                addAvailability()
        
            case 3:
                removeAvailability()
        
            case 4:
                viewMember()
        
            case 5:
                break
        
                

#-----ADMIN FUNTIONS-----#
def manageBookings():
    return

def monitorEquip():
    return

def updateClass():
    return

def processingBilling():
    return

#Log in as Admin
def adminLogin():

    #Login using ID
        #If failed return
        #return

    #If success
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("1. Manage room bookings")
        print("2. Monitor equipment maintenance")
        print("3. Update class schedule")
        print("4. Process billing and payment")
        print("5. Log out")

        operation = int(input("Please choose an operation"))

        match(operation):
            case 1:
                manageBookings()

            case 2:
                monitorEquip()
        
            case 3:
                updateClass()
        
            case 4:
                processingBilling()
        
            case 5:
                break
        



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