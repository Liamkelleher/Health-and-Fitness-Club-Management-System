import connection as connect
import clubMember as member
import trainer as trainer
import admin as admin

#-----MAIN FLOW-----#

connect.initData()

while True:

    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
    print("1. Register new Club Member")
    print("2. Log in as Club Member")
    print("3. Register new Trainer")
    print("4. Log in as Trainer")
    print("5. Register new Administrative Staff")
    print("6. Log in as Administrative Staff")
    print("7. Quit")
    
    operation = int(input("Please choose an operation: "))

    match(operation):

        case 1:
            member.registerNewMember()

        case 2: 
            member.clubMemberLogin()

        case 3:
            trainer.registerNewTrainer()

        case 4:
            trainer.trainerLogin()

        case 5:
            admin.registerNewTrainer()

        case 6:
            admin.adminLogin()

        case 7: 
            break

#Close cursor and connection
connection, cursor = connect.connect()
cursor.close()
connection.close()
