#-----TRAINER FUNTIONS-----#

def viewAvailibity():
    return

def addAvailability():
    return

def removeAvailability():
    return

def viewMember():
    return

#Log in as Trainer
def trainerLogin():

    #Login using ID
        #If failed return
        #return

    #If success
    while True:
        print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("1. View availabity")
        print("2. Add availability")
        print("3. Remove availability")
        print("4. View member")
        print("5. Log out")

        operation = int(input("Please choose an operation"))

        match(operation):
            case 1:
                viewAvailibity()
                
            case 2:
                addAvailability()
        
            case 3:
                removeAvailability()
        
            case 4:
                viewMember()
        
            case 5:
                break
        
                