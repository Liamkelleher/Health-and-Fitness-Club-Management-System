import connection as database
#-----MEMBER FUNTIONS-----#

#Add new Club Member
def registerNewMember():

    return

#1. Update personal information
#update email
def updateEmail(id, newEmail):
    return

#update password
def updatePassword(id, newPassword):
    return

#2. add fitness achievements
def updateAchievements(id, achievement):
    return

#3. Update health statistics
def updateStats(id):
    return

#4. Update health statistics
def updateGoals(id):
    return

#5. Display dashboard
def displayDashboard(id):
    return

#6. Schedule personal training session
def scheduleTraining():
    return

#7. Reschedule personal training session
def rescheduleTraining():
    return

#8. Cancel personal training session
def cancelTraining():
    return

#9. Participate in class
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
        print("1. Update personal information")
        print("2. Add fitness achievements")
        print("3. Update health statistics")
        print("4. Update Goals")
        print("5. Display dashboard")
        print("6. Schedule personal training session")
        print("7. Reschedule personal training session")
        print("8. Cancel personal training session")
        print("9. Participate in class")
        operation = int(input("Please choose an operation: "))

        match(operation):
            case 0: 
                break

            case 1: #1. Update personal information
                print("1. Update email")
                print("2. Update password")
                choice = int(input("Please choose what you wish to update: "))
                match(choice):
                    case 1:
                        newEmail = input("Please input your new email")
                        updateEmail(id, newEmail)
                    case 2:
                        newPassword = input("Please input your new password")
                        updatePassword(id, newPassword)

            case 2: #2. add fitness achievements
                achievement = input("Input your new achievement!")
                addAchievements(id, achievement)

            case 3:
                updateStats()

            case 4:
                updateGoals()

            case 5:
                displayDashboard()

            case 6:
                scheduleTraining()

            case 7:
                rescheduleTraining()

            case 8:
                cancelTraining()

            case 9:
                participateInClass()
                  
