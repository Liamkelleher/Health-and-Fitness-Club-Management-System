import connection as database
#-----MEMBER FUNTIONS-----#

#Add new Club Member
def registerNewMember():

    return

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

def verification():

    #Get data
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("Club Member Login:\n")
    email = input("Enter your email:    ")
    password = input("Enter your password: ")

    #Check data
    query = """
    SELECT memberid, fName, lName FROM clubmember
    WHERE email=%s AND password=%s;
    """
    result = database.login(query, (email, password))

    #If not
    if(result == []):
        return False, None, None, None
    
    #If works
    return True, result[0], result[1], result[2]

#Log in as Club Member
def clubMemberLogin():

    #Check if member in the system
    verify, id, fName, lName = verification()

    if(verify == False):
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("\nLogin unsuccessful\n")
        return

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"\nLogin successful.\nWelcome back Club Member # {id}: {fName} {lName}!\n")

    #If success
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("0. Logout")
        print("1. Update person information")
        print("2. Update fitness achievements")
        print("3. Update health statistics")
        print("4. Display dashboard")
        print("5. Schedule personal training session")
        print("6. Reschedule personal training session")
        print("7. Cancel personal training session")
        print("8. Participate in class")
        operation = int(input("Please choose an operation: "))

        match(operation):
            case 0: 
                break

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
                  
