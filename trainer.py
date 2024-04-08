import connection as database

#-----TRAINER FUNTIONS-----#

# helper for executing queries
def executeQuery(query, parameters=()):
    connection, cursor = database.connect()
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

def viewAvailibity(trainerID, trainerName):
    query = """
    SELECT day, startTime, endTime, isFree
    FROM Availabilities
    WHERE trainerID = %s
    """
    results = executeQuery(query, (trainerID,))

    print(f"{trainerName}'s AVAILABILITY:")
    for day in results:
        print("-----------------------------------------------------------")
        print(f"Day: {day[0]}, Start Time: {day[1]}, End Time: {day[2]}, Is Free?: {day[3]}")
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

    executeQuery(query, (trainerID, day, startTime, endTime, isFree))

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

    executeQuery(query, (isFree, trainerID))

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

    executeQuery(query, (trainerID, day, startTime, endTime, isFree))

    print("Availability removed successfully.")
    return

def viewMember():
    return

# Log in as Trainer
def trainerLogin():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    

    query = """
    SELECT trainerID, fName, lName FROM Trainer
    WHERE email = %s AND password = %s;
    """

    connection, cursor = database.connect()
    cursor.execute(query, (email, password))
    
    result = cursor.fetchone()
    
    if result:
        trainerID, trainerName, trainerLastName = result
        print(f"Login successful.\nWelcome back {trainerID}: {trainerName} {trainerLastName}!")
    else:
        print("Login failed. Please try again.")
        return

    connection.commit()
    cursor.close()
    connection.close()

    # once logged in, can perform trainer operations
    trainerOperations(trainerID, trainerName)

def trainerOperations(trainerID, trainerName):
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("1. View availabity")
        print("2. Add availability")
        print("3. Update availability")
        print("4. Remove availability")
        print("5. View member")
        print("6. Log out")

        operation = int(input("Please choose an operation: "))

        match(operation):
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
        
            case 6:
                break
        
                