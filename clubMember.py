import connection as database
#-----MEMBER FUNTIONS-----#

#Add new Club Member
def registerNewMember():
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("User registration:\n ")

    email = input("Enter email:      ")
    password = input("Enter password:   ")
    fName = input("Enter first name: ")
    lName = input("Enter last name:  ")

    query = "INSERT INTO ClubMember (email, password, fName, lName) VALUES(%s, %s, %s, %s);"
    database.executeQuery(query, (email, password, fName, lName))
    return

#1. Update personal information
#update email
def updateEmail(id):
    newEmail = input("Please input your new email")
    query = "UPDATE ClubMembers SET email = %s WHERE memberID = %s;"
    database.executeQuery(query, (newEmail, id))
    return

#update password
def updatePassword(id):
    newPassword = input("Please input your new password")
    query = "UPDATE ClubMembers SET password = %s WHERE memberID = %s;"
    database.executeQuery(query, (newPassword, id))
    return

#2. add fitness achievements
def addAchievements(id):
    achievement = input("Input your new achievement! ")
    query = """INSERT INTO Achievements (memberID, achievement)
                VALUES (%s, %s)"""
    database.executeQuery(query, (id, achievement))
    return

#3. Update health statistics
def updateStats(id, restingHR, weight, height):
    query = "UPDATE Dashboard SET restingHeartRate = %s, weight = %s, height =%s WHERE memberID=%s"
    database.executeQuery(query, (restingHR, weight, height, id))
    return

#4. Update goals
def updateGoals(id, weightGoal, timeGoal):
    query = "UPDATE DashBoard SET weightGoal = %s, timeGoal = %s WHERE memberID=%s"
    database.executeQuery(query, (weightGoal, timeGoal, id))
    return

#5. Update routines
def addRoutine(id, routine):
    query = "INSERT INTO Routines (memberID, routine) VALUES (%s, %s)"
    database.executeQuery(query, (id, routine))
    return

#6 Remove routines
def removeRoutine(id, routine):
    return

#6. Display dashboard
def displayDashboard(id):
    query = """SELECT * FROM dashboard 
            WHERE memberid=%s"""
    result = database.executeQuery(query, (id,))
    result = result[0]
    
    #Display main dashboard
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("---Personal Dashboard---\n")
    print("Member ID:           ", result[0])
    print("Resting Heart Rate:  ", result[1])
    print("Current weight:      ", result[2])
    print("Current height:      ", result[3])
    print("Current weight goal: ", result[4])
    print("Current time goal:   ", result[5])

    #Display achievements
    query = """SELECT achievement FROM achievements
            WHERE memberid=%s"""
    result = database.executeQuery(query, (id,))

    print("\nAchievements: ")
    for achievement in result:
        print(" -", achievement[0])


    #Display routines
    query = """SELECT routine FROM routines
            WHERE memberid=%s"""
    result = database.executeQuery(query, (id,))
    print("\nRoutines: ")
    for routine in result:
        print(" -", routine[0])

    return

#6. Schedule personal training session
def scheduleTraining(id, option):
    choice = int(input("type in the training session option number: ")) - 1
    result = option[choice]
    return

#8. Reschedule personal training session
def rescheduleTraining():
    return

#9. Cancel personal training session
def cancelTraining():
    return

#10. Participate in class
def participateInClass():
    return

#11. Cancel class
def cancelClass():
    return


def viewAvailableTrainingSessions():
    query = """SELECT t.fName, t.lName, a.day, a.startTime, a.endTime
                FROM Trainer t JOIN Availabilities a ON t.trainerID = a.trainerID
                WHERE a.isFree = TRUE
                GROUP BY t.fName, t.lName, a.isFree, a.day, a.startTime, a.endTime"""
    result = database.executeQuery(query)
    for possibleTS in result:
        i = 1
        print("- - - - - - - - - - - - - - - - - - - -")
        print("Available option: ", i)
        print("Trainer: ", possibleTS[0], " ", possibleTS[1])
        print("Date: ", possibleTS[2])
        print("Time: ", possibleTS[3], "-", possibleTS[4])
        i += 1
    return result

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
        print("0.  Logout")
        print("1.  Update personal information")
        print("2.  Add fitness achievements")
        print("3.  Update health statistics")
        print("4.  Update Goals")
        print("5.  Add a routine")
        print("6.  Remove a routine")
        print("7.  Display dashboard")
        print("8.  Schedule personal training session")
        print("9.  Reschedule personal training session")
        print("10. Cancel personal training session")
        print("11. Participate in class")
        print("12. Cancel class")
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
                        updateEmail(id)
                    case 2:
                        updatePassword(id)

            case 2: #2. add fitness achievements
                addAchievements(id)

            case 3:
                updateStats(id,)

            case 4:
                updateGoals()

            case 5:
                routine = input("Please enter in your routine: ")
                addRoutine(id, routine)

            case 6: 
                routine = input("What routine would you like to remove? ")

            case 7:
                displayDashboard(id)

            case 6:
                option = viewAvailableTrainingSessions()
                
                scheduleTraining(id, option)

            case 9:
                rescheduleTraining()

            case 10:
                cancelTraining()

            case 11:
                participateInClass()
            
            case 12:
                cancelClass()

                
                  
