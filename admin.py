import connection as database

#-----ADMIN FUNTIONS-----#
def manageBookings():

    connection, cursor = database.connect()

    id = input("Class ID to update? ")

    roomNum = input("New room number:    ")

    cursor.execute("""UPDATE class
                    SET roomNum=%s
                    WHERE classid=%s""", (roomNum, id))
    
    connection.commit()
    connection.close()
    cursor.close()

    return

def monitorEquip():
    connection, cursor = database.connect()
    cursor.execute("""SELECT * from trainingEquipment""")

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("TRAINING EQUIPMENT:")

    for equip in cursor.fetchall():
        print("- - - - - - - - - -")
        print("ID:     ", equip[0])
        print("Name:   ", equip[1])
        print("Status: ", equip[2])

    connection.close()
    cursor.close()
    return

def addClass():
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    roomNum = input("Choose a room #:               ")
    spots = input("Choose # of spots:             ")
    type = input("Choose type of class:          ")
    day = input("Choose day <yyyy-mm-dd>:       ")
    sTime = input("Choose start time <hh-mm-ss>:  ")
    eTime = input("Choose end time <hh:mm:ss>:    ")

    connection, cursor = database.connect()

    cursor.execute("""INSERT INTO class(roomnum, spots, type, day, starttime, endtime) VALUES
                   (%s, %s, %s, %s, %s, %s)""", (roomNum, spots, type, day, sTime, eTime))
    
    connection.commit()

    connection.close()
    cursor.close()

    return

def updateClass():
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("1. Change class schedule")
    print("2. Remove class")

    operation = input("Please choose an operation: ")
    print()
    
    connection, cursor = database.connect()

    if(operation == '1'):

        id = input("Class ID to update? ")

        sTime = input("New start time:     ")
        eTime = input("New end time:       ")

        cursor.execute("""UPDATE class
                       SET starttime=%s, endtime=%s
                       WHERE classid=%s""", (sTime, eTime, id))
        
        connection.commit()
        connection.close()
        cursor.close()

    else:

        id = input("What classID do you wish to remove? ")

        cursor.execute("""DELETE FROM class
                        WHERE classId=%s""", (id))
        
        connection.commit()
        connection.close()
        cursor.close()

    return

def viewClasses():
    connection, cursor = database.connect()
    cursor.execute("""SELECT * from Class""")

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("CLASSES:")

    for each in cursor.fetchall():
        print("- - - - - - - - - -")
        print("ID:              ", each[0])
        print("Room #:          ", each[1])
        print("Available Spots: ", each[2])
        print("Class type:      ", each[3])
        print("Day              ", each[4])
        print("Time:            ", each[5], "-", each[6])

    connection.close()
    cursor.close()
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
        print("3. Add class schedule")
        print("4. Update class schedule")
        print("5. View classes")
        print("6. Process billing and payment")
        print("7. Log out")

        operation = int(input("Please choose an operation: "))

        match(operation):
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
        
            case 7:
                break
        


