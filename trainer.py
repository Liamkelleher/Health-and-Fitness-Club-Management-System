import connection as database
import clubMember as clubMember

#-----TRAINER FUNTIONS-----#

# Lists all availabilities for current trainer
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
        print(f"ID: {day[0]} || Day: {day[1]}, Start Time: {day[2]}, End Time: {day[3]}, Is Free? {day[4]}")
    return

# prompts trainer to enter a new availability block
def addAvailability(trainerID):
    day = input("Enter Day (YYYY-MM-DD): ")
    startTime = input("Enter Start Time (HH:MM): ") + ":00"
    endTime = input("Enter End Time (HH:MM): ") + ":00"

    query = """
    INSERT INTO Availabilities (trainerID, day, startTime, endTime, isFree)
    VALUES (%s, %s, %s, %s, %s)
    """

    database.executeQuery(query, (trainerID, day, startTime, endTime, True))

    print("Availability updated successfully.")
    return


# Trainer can modify availability between 'free' or 'busy'
def updateAvailability(trainerID, trainerName):
    viewAvailibity(trainerID, trainerName)

    availability = input("\nSelect availability ID to modify: ")

    # select avilability matching inputted ID
    query = """
    SELECT availabilityID, day, startTime, endTime, isFree
    FROM Availabilities
    WHERE trainerID = %s AND availabilityID = %s
    """
    results = database.executeQuery(query, (trainerID, availability))
    for result in results:
        print(f"\nAvailability on {result[1]}, Start Time: {result[2]}, End Time: {result[3]}, Is Free? {result[4]}")
   
    print("\nUpdate selected availability below:")
    isFree = (input("Free(1) or Busy(0)? "))

    query = """
    UPDATE Availabilities 
    SET isFree = %s
    WHERE trainerID = %s
    """

    database.executeQuery(query, (isFree, trainerID))

    print("\nAvailability updated successfully.")
    return

# trainer can remove selected availability
def removeAvailability(trainerID, trainerName):
    viewAvailibity(trainerID, trainerName)

    availability = input("\nSelect availability ID to delete: ")

    # select avilability matching inputted ID
    query = """
    SELECT availabilityID, day, startTime, endTime, isFree
    FROM Availabilities
    WHERE trainerID = %s AND availabilityID = %s
    """
    results = database.executeQuery(query, (trainerID, availability))
    for result in results:
        print(f"Selected: Availability on {result[1]}, Start Time: {result[2]}, End Time: {result[3]}, Is Free? {result[4]}")
    
    print("\nDeleting....")

    query = """
    DELETE FROM Availabilities 
    WHERE trainerID = %s AND availabilityID = %s
    """
    database.executeQuery(query, (trainerID, availability))

    print("\nAvailability deleted successfully.")
    return

# trainer can view a member by name
def viewMember():
    query = """
    SELECT memberid, fname, lname, email
    FROM ClubMember
    """
    results = database.executeQuery(query)

    print(f"\nClub Members:")
    for member in results:
        print("-------------------------------------")
        print(f"Club Member id:{member[0]} Name:{member[1]} {member[2]} Email:{member[3]}")

    selection = input("\nSelect a club member to view (id): ")

    clubMember.displayDashboard(selection)

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

def trainerLogin():

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
                viewAvailibity(id, fName + " " + lName)
                
            case 2:
                addAvailability(id)
            
            case 3:
                updateAvailability(id, fName + " " + lName)
        
            case 4:
                removeAvailability(id, fName + " " + lName)
        
            case 5:
                viewMember()
        
        
                