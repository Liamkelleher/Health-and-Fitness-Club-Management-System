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
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    newEmail = input("Please input your new email: ")
    query = "UPDATE ClubMember SET email = %s WHERE memberID = %s;"
    database.executeQuery(query, (newEmail, id))
    return

#update password
def updatePassword(id):
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    newPassword = input("Please input your new password: ")
    query = "UPDATE ClubMember SET password = %s WHERE memberID = %s;"
    database.executeQuery(query, (newPassword, id))
    return

#2. add fitness achievements
def addAchievements(id):
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    achievement = input("Input your new achievement! ")
    query = """INSERT INTO Achievements (memberID, achievement)
                VALUES (%s, %s)"""
    database.executeQuery(query, (id, achievement))
    return

#3. Update health statistics
def updateStats(id):
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("0. Quit")
        print("1. Resting heart rate")
        print("2. Weight")
        print("3. Height")
        operation = int(input("What would you like to change? "))

        match(operation):
            case 0:
                break

            case 1:
                resthr = input("\nNew resting heart rate: ")
                query = """UPDATE dashboard 
                        SET resthr=%s
                        WHERE memberid=%s"""
                database.executeQuery(query, (resthr, id))
            case 2: 
                weight = input("\nNew weight (lbs): ")
                query = """UPDATE dashboard 
                        SET weight=%s
                        WHERE memberid=%s"""
                database.executeQuery(query, (weight, id))

            case 3:
                height = input("\nNew height (cm): ")
                query = """UPDATE dashboard 
                        SET height=%s
                        WHERE memberid=%s"""
                database.executeQuery(query, (height, id))

    return

#4. Update goals
def updateGoals(id):
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    weightGoal = input("What is your new weight goal?                           ")
    timeGoal = input("What day do you want to achieve this goal (YYYY-MM-DD)? ")
    query = "UPDATE DashBoard SET weightGoal = %s, timeGoal = %s WHERE memberID=%s"
    database.executeQuery(query, (weightGoal, timeGoal, id))
    return

#5. Update routines
def addRoutine(id):
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    routine = input("Please enter in your routine: ")
    query = "INSERT INTO Routines (memberID, routine) VALUES (%s, %s)"
    database.executeQuery(query, (id, routine))
    return

#6. Remove routines
def removeRoutine(id):
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    routine = input("What routine would you like to remove? ")
    query = """DELETE from routines
            WHERE memberid=%s AND routine=%s"""
    database.executeQuery(query, (id, routine))
    return

#7. Display dashboard
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

    print("- - - - - - - - - - - - - - - - - - - -")
    print("Achievements: \n")
    for achievement in result:
        print(" -", achievement[0])

    #Display routines
    query = """SELECT routine FROM routines
            WHERE memberid=%s"""
    result = database.executeQuery(query, (id,))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("Routines: \n")
    for routine in result:
        print(" -", routine[0])

    #Display billing
    query = """SELECT membership, trainingsession, otherservices 
            FROM billing
            WHERE memberid=%s"""
    result = database.executeQuery(query, (id,))
    result = result[0]
    print("- - - - - - - - - - - - - - - - - - - -")
    print("Billing: \n")
    print("Monthly:           " + "$" + str(result[0]))
    print("Training Sessions: " + "$" + str(result[1]))
    print("Other services:    " + "$" + str(result[2]))

    #Display schedule
    
    query = """SELECT s.scheduleid, t.fName, t.lName, a.day, a.startTime, a.endTime
            FROM trainer t JOIN availabilities a ON t.trainerid=a.trainerid
            JOIN trainingsession s ON s.scheduleid=a.availabilityid
            WHERE s.memberid=%s"""
    
    result = database.executeQuery(query, (id,))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("Training Sessions: ")
    for schedule in result:
        print("Schedule ID:  ", schedule[0])
        print("Trainer name: ", schedule[1] + " " + schedule[2])
        print("Date:         ", schedule[3])
        print("Time:         ", schedule[4], "-", schedule[5])
        print()
    
    #Display classes
    query = """SELECT c.classid, c.roomNum, c.day, c.type, c.startTime, c.endTime
            FROM class c JOIN participatesIn p 
            ON c.classid=p.classid
            WHERE p.memberid=%s
            ORDER BY c.day, c.startTime ASC"""
    result = database.executeQuery(query, (id,))
    print("- - - - - - - - - - - - - - - - - - - -")
    print("Classes: ")
    for classes in result:
        print("Class ID: ", classes[0])
        print("Room #:   ", classes[1])
        print("Date:     ", classes[2])
        print("Type:     ", classes[3])
        print("Time:     ", classes[4], "-", classes[5])
        print()
    return


#8. Schedule personal training session
def viewAvailableTrainingSessions():
    query = """SELECT a.availabilityID, t.fName, t.lName, a.day, a.startTime, a.endTime
                FROM Trainer t JOIN Availabilities a ON t.trainerID = a.trainerID
                WHERE a.isFree = TRUE
                ORDER BY a.day, a.startTime ASC"""
    result = database.executeQuery(query)
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("Schedules: \n")
    for possibleTS in result:
        print("- - - - - - - - - - - - - - - - - - - -")
        print("Schedule ID: ", possibleTS[0])
        print("Trainer: ", possibleTS[1] + " " + possibleTS[2])
        print("Date: ", possibleTS[3])
        print("Time: ", possibleTS[4], "-", possibleTS[5])

def scheduleTraining(id):
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")

    choice = input("Input the schedule ID of the training session: ")
    
    query = """INSERT INTO TrainingSession(scheduleid, memberid) VALUES
            (%s, %s)"""
    database.executeQuery(query, (choice, id))

    return

#9. Reschedule personal training session
def rescheduleTraining(id):
    #show current training sessions
    query = """SELECT ts.scheduleID, t.fName, t.lName, a.day, a.startTime, a.endTime 
            FROM TrainingSession ts JOIN availabilities a ON ts.scheduleid = a.availabilityID
            JOIN Trainer t ON a.trainerID=t.trainerID
            WHERE memberID = %s
            ORDER BY a.day, a.startTime ASC"""
    result = database.executeQuery(query, (id,))

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("Training Sessions: \n")
    #print out training sessions of the club member
    for trainingSession in result:
        print("- - - - - - - - - - - - - - - - - - - -")
        print("Schedule ID: ", trainingSession[0])
        print("Trainer: ", trainingSession[1] + " " + trainingSession[2])
        print("Date: ", trainingSession[3])
        print("Time: ", trainingSession[4], "-", trainingSession[5])
    
    print("- - - - - - - - - - - - - - - - - - - -")
    choiceReschedule = input("Input the schedule ID of the training session to reschedule: ")
    #-----------------------------------------------------------------------------------------
    #show the available training sesssions
    viewAvailableTrainingSessions()

    #ask club member which new training session they would like to take instead
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    choice = int(input("Input the schedule ID of the new training session: "))
    
    #-----------------------------------------------------------------------------------------
    #REWORK THE TRAINING SESSIONS
    #add the training session
    query = """INSERT INTO TrainingSession (scheduleID, memberID)
                VALUES (%s, %s)"""
    database.executeQuery(query, (choice, id))

    #delete the current training session
    query = "DELETE FROM TrainingSession WHERE scheduleID = %s"
    database.executeQuery(query, (choiceReschedule,))

    return

#10. Cancel personal training session
def cancelTraining(id):
    query = """SELECT ts.scheduleID, t.fName, t.lName, a.day, a.startTime, a.endTime 
            FROM TrainingSession ts JOIN availabilities a ON ts.scheduleid = a.availabilityID
            JOIN Trainer t ON a.trainerID=t.trainerID
            WHERE memberID = %s
            ORDER BY a.day, a.startTime ASC"""
    result = database.executeQuery(query, (id,))

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("Training Sessions: \n")
    #print out training sessions of the club member
    for trainingSession in result:
        print("- - - - - - - - - - - - - - - - - - - -")
        print("Schedule ID: ", trainingSession[0])
        print("Trainer: ", trainingSession[1] + " " + trainingSession[2])
        print("Date: ", trainingSession[3])
        print("Time: ", trainingSession[4], "-", trainingSession[5])
    
    print("- - - - - - - - - - - - - - - - - - - -")
    choice = int(input("Input the ID of the training session to cancel: "))

    query = "DELETE FROM TrainingSession WHERE scheduleID = %s"
    database.executeQuery(query, (choice,))
    return

#11. Participate in class
def participateInClass(id):
    query = """SELECT c.classID, c.roomNum, c.spots, c.type, c.day, c.startTime, c.endTime
            FROM Class c
            LEFT JOIN ParticipatesIn p ON c.classID = p.classID AND p.memberID = %s
            WHERE p.memberID IS NULL and spots>0"""
    result = database.executeQuery(query, (id,))

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    if(len(result) == 0):
        print("\nNo classes available\n")
        return
    
    print("\nAvailable Classes:")
    for classes in result:
        print("Class ID: ", classes[0])
        print("Room #:   ", classes[1])
        print("Spots:    ", classes[2])
        print("Type:     ", classes[3])
        print("Date:     ", classes[4])
        print("Time:     ", classes[5], "-", classes[6])
        print()

    print("- - - - - - - - - - - - - - - - - - - -")
    choice = input("Input the ID of the class you would like to join: ")

    query = """INSERT INTO participatesin (memberID, classID)
            VALUES (%s, %s)"""
    
    database.executeQuery(query, (id, choice))

    return

#12. Cancel class
def cancelClass(id):
    query = """SELECT c.classid, c.roomNum, c.type, c.day, c.startTime, c.endTime
            FROM class c JOIN participatesIn p 
            ON c.classid=p.classid
            WHERE p.memberid=%s
            ORDER BY c.day, c.startTime ASC"""
    result = database.executeQuery(query, (id,))
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("Classes: ")
    for classes in result:
        print("Class ID: ", classes[0])
        print("Room #:   ", classes[1])
        print("Type:     ", classes[2])
        print("Date:     ", classes[3])
        print("Time:     ", classes[4], "-", classes[5])
        print()

    print("- - - - - - - - - - - - - - - - - - - -")
    choice = int(input("Input the ID of the class to cancel: "))

    query = """DELETE FROM participatesin 
            WHERE classid=%s AND memberid=%s"""
    database.executeQuery(query, (choice, id))
    
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
                updateGoals(id,)

            case 5:
                addRoutine(id)

            case 6: 
                removeRoutine(id)

            case 7:
                displayDashboard(id)

            case 8:
                viewAvailableTrainingSessions()
                
                scheduleTraining(id)

            case 9:
                rescheduleTraining(id)

            case 10:
                cancelTraining(id)

            case 11:
                participateInClass(id)
            
            case 12:
                cancelClass(id)

                
                  
