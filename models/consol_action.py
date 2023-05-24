from models.user import *
from models.contact import *
from models.contract import *
from models.lead import *
from models.product import *

class UserAction:
    @classmethod
    def login_user(cls):
        print('Welcome to CRMBanking')
        username1 = input('Enter your name (username): ')
        password1 = input('Enter password: ')
        allusers = User.select().where(User.username == username1).limit(1)
        if len(allusers) != 1:
            print("User or password incorrect!")
        user = allusers[0]
        if user.username == username1:
            if user.password == password1:
                print('Hi, ', username1)
                print("User is logged in") # LOG start session
                return True
            else:
                print('User or password incorrect!')
                return False
        return False

    @classmethod
    def section(cls):
        print("Choose section!")
        action = input("1 - Contacts, 2 - Contracts, 3 - Leads, 4 - Users, 5 - Products, 0 - Exit: ")
        return action

    @classmethod
    def operation(cls):
        print("Choose operation!")
        action = input(f"1 - Create, 2 - Get, 3 - Import from file, 4 - Export in file, 5 - Sign, "
                       f"9 - Go to Section, 0 - Exit: ")
        return action

    @classmethod
    def operation_create_user(cls):
        username1 = input('Enter username: ')
        password1 = input('Enter password: ')
        msg = create_user(username=username1, password=password1)
        return print(msg)

    @classmethod
    def operation_get_user(cls):
        msgs = get_users()
        print("All users (Id, Created, Username, Password):")
        for msg in msgs:
            print(msg.id, msg.created, msg.username, msg.password)


    #create contact