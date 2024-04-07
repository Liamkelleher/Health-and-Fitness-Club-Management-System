import connection as database

#-----ADMIN FUNTIONS-----#
def manageBookings():
    return

def monitorEquip():
    return

def updateClass():
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
        print("3. Update class schedule")
        print("4. Process billing and payment")
        print("5. Log out")

        operation = int(input("Please choose an operation"))

        match(operation):
            case 1:
                manageBookings()

            case 2:
                monitorEquip()
        
            case 3:
                updateClass()
        
            case 4:
                processingBilling()
        
            case 5:
                break
        


