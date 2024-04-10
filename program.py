import connection as connect
import clubMember as member
import trainer as trainer
import admin as admin

#-----MAIN FLOW-----#

while True:

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("0. Quit")
    print("1. Register new Club Member")
    print("2. Log in as Club Member")
    print("3. Log in as Trainer")
    print("4. Log in as Administrative Staff")
    
    operation = int(input("Please choose an operation: "))

    match(operation):
        case 0: 
            break

        case 1:
            member.registerNewMember()

        case 2: 
            member.clubMemberLogin()

        case 3:
            trainer.trainerLogin()

        case 4:
            admin.adminLogin()

