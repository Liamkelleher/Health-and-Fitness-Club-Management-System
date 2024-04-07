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
