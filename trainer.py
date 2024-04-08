import connection as database

#-----TRAINER FUNTIONS-----#

def viewAvailibity(trainerID, trainerName):
    query = """
    SELECT availabilityID, day, startTime, endTime, isFree
    FROM Availabilities
    WHERE trainerID = %s
    """
    results = database.executeQuery(query, (trainerID,))

    print(f"\n{trainerName}'s AVAILABILITY:")
    for day in results:
        print("-----------------------------------------------------------------------------------")
        print(f"ID: {day[0]} || Day: {day[1]}, Start Time: {day[2]}, End Time: {day[3]}, Is Free?: {day[4]}")
    return

def addAvailability(trainerID):
    day = input("Enter Day (YYYY-MM-DD): ")
    startTime = input("Enter Start Time (HH:MM): ") + ":00"
    endTime = input("Enter End Time (HH:MM): ") + ":00"
    isFree = (input("Free(1) or Busy(0)? "))

    query = """
    INSERT INTO Availabilities (trainerID, day, startTime, endTime, isFree)
    VALUES (%s, %s, %s, %s, %s)
    """

    database.executeQuery(query, (trainerID, day, startTime, endTime, isFree))

    print("Availability updated successfully.")
    return

### ADD AVAILABILITY ID EASIER TO MODIFY/ DELETE
def updateAvailability(trainerID, trainerName):
    viewAvailibity(trainerID, trainerName)

    day = input("Enter Day (YYYY-MM-DD): ")
    startTime = input("Enter Start Time (HH:MM): ") + ":00"
    endTime = input("Enter End Time (HH:MM): ") + ":00"
    isFree = (input("Free(1) or Busy(0)? "))

    query = """
    UPDATE Availabilities 
    SET isFree = %s
    WHERE trainerID = %s
    """

    database.executeQuery(query, (isFree, trainerID))

    print("Availability updated successfully.")
    return

def removeAvailability(trainerID):
    day = input("Enter Day (YYYY-MM-DD): ")
    startTime = input("Enter Start Time (HH:MM)") + ":00"
    endTime = input("Enter End Time (HH:MM): ") + ":00"
    isFree = True

    query = """
    INSERT INTO Availabilities (trainerID, day, startTime, endTime, isFree)
    VALUES (%s, %s, %s, %s, %s)
    """

    database.executeQuery(query, (trainerID, day, startTime, endTime, isFree))

    print("Availability removed successfully.")
    return

def viewMember():
    return

# Log in as Trainer
def verification():

    #Get data
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("Trainer Login:\n")
    email = input("Enter your email:    ")
    password = input("Enter your password: ")

    #Check data
    query = """
    SELECT trainerid, fName, lName FROM trainer
    WHERE email=%s AND password=%s;
    """
    result = database.login(query, (email, password))

    #If not
    if(result == []):
        return False, None, None, None
    
    #If works
    return True, result[0], result[1], result[2]

    return

def trainerOperations(trainerID, trainerName):

    #Check if admin in the system
    verify, id, fName, lName = verification()

    if(verify == False):
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("\nLogin unsuccessful\n")
        return

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"\nLogin successful.\nWelcome back Trainer # {id}: {fName} {lName}!\n")

    while True:
        print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("0. Log out")
        print("1. View availabity")
        print("2. Add availability")
        print("3. Update availability")
        print("4. Remove availability")
        print("5. View member")

        operation = int(input("Please choose an operation: "))

        match(operation):
            case 0:
                break

            case 1:
                viewAvailibity(trainerID, trainerName)
                
            case 2:
                addAvailability(trainerID)
            
            case 3:
                updateAvailability(trainerID, trainerName)
        
            case 4:
                removeAvailability(trainerID)
        
            case 5:
                viewMember()
        
        
                