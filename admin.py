import connection as database

#-----ADMIN FUNTIONS-----#

def manageBookings():

    viewClasses()

    #Get id and room number to update to
    id = input("Class ID to update? ")
    roomNum = input("New room number:    ")

    query = """UPDATE class
            SET roomNum=%s
            WHERE classid=%s"""
    database.executeQuery(query, (roomNum, id))

    return

#Check equipment
def monitorEquip():
    
    #Get equipment
    query = """SELECT * from trainingEquipment"""
    result = database.executeQuery(query)

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("TRAINING EQUIPMENT:")

    #Print all equipment
    for equip in result:
        print("- - - - - - - - - -")
        print("ID:     ", equip[0])
        print("Name:   ", equip[1])
        print("Status: ", equip[2])

    return

#Check if class is available
def checkClass(day):

    #If class with that room number and day exists
    query = """SELECT COUNT(*) FROM class 
            WHERE day=%s"""

    result = database.executeQuery(query, (day,))

    #Doesn't exists
    if(result[0][0] == 0):

        return True
    
    #Exists
    return False

#Add a class schedule
def addClass():
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

    while True:
        day = input("Choose day (YYYY-MM-DD): ")
        
        #If class already exists that day
        if(checkClass(day)):

            break

        #If room is not free
        else:
            
            print("\n*Room is not available that day, try another room and day*\n")

    roomNum = input("Choose a room #:               ")
    sTime = input("Choose start time (HH:MM):     ") + ":00"
    eTime = input("Choose end time (HH:MM):       ") + ":00"
    spots = input("Choose # of spots:             ")
    type = input("Choose type of class:          ")

    query = """INSERT INTO class(roomnum, spots, type, day, starttime, endtime) VALUES
                   (%s, %s, %s, %s, %s, %s)"""

    #Add room 
    database.executeQuery(query, (roomNum, spots, type, day, sTime, eTime))

    return

#Change time of class or remove class
def updateClass():
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("1. Change class schedule")
    print("2. Remove class")

    operation = input("Please choose an operation: ")
    print()

    viewClasses()

    #Change time
    if(operation == '1'):

        #Get class and new time
        id = input("Class ID to update?     ")

        sTime = input("New start time (HH:MM): ") + ":00"
        eTime = input("New end time (HH:MM):   ") + ":00"

        query = """UPDATE class
                SET starttime=%s, endtime=%s
                WHERE classid=%s"""
        
        database.executeQuery(query, (sTime, eTime, id))

    #Remove class
    else:

        #Get class
        id = input("What class ID do you wish to remove? ")

        #Remove
        query = """DELETE FROM class
                WHERE classId=%s"""
        database.executeQuery(query, id)

    return

#View all classes
def viewClasses():

    #Get classes
    query = """SELECT * from Class
            ORDER BY day, startTime ASC"""
    results = database.executeQuery(query)

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("CLASSES:")

    #Print all classes
    for each in results:
        print("- - - - - - - - - -")
        print("ID:              ", each[0])
        print("Room #:          ", each[1])
        print("Available Spots: ", each[2])
        print("Class type:      ", each[3])
        print("Day              ", each[4])
        print("Time:            ", each[5], "-", each[6])

    return

def processingBilling():
    query = """UPDATE billing
            SET trainingsession=0, otherservices=0"""
    database.executeQuery(query)
    return

def verification(): 

    #Get data
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("Admin Login:\n")
    email = input("Enter your email:    ")
    password = input("Enter your password: ")

    #Check data
    query = """
    SELECT adminid, fName, lName FROM admin
    WHERE email=%s AND password=%s;
    """
    result = database.login(query, (email, password))

    #If not
    if(result == []):
        return False, None, None, None
    
    #If works
    return True, result[0], result[1], result[2]

#Log in as Admin
def adminLogin():

    #Check if admin in the system
    verify, id, fName, lName = verification()

    if(verify == False):
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("\nLogin unsuccessful\n")
        return

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"\nLogin successful.\nWelcome back Admin # {id}: {fName} {lName}!\n")

    #If success
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("0. Log out")
        print("1. Manage room bookings")
        print("2. Monitor equipment maintenance")
        print("3. Add class schedule")
        print("4. Update class schedule")
        print("5. View classes")
        print("6. Process billing and payment")

        operation = int(input("Please choose an operation: "))

        match(operation):
            case 0:
                break

            case 1:
                manageBookings()

            case 2:
                monitorEquip()
        
            case 3:
                addClass()

            case 4:
                updateClass()

            case 5:
                viewClasses()
        
            case 6:
                processingBilling()
        
        


