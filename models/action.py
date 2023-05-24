from models.user import *

class UserAction:
    @classmethod
    def login_user(cls):
        username1 = input('Enter your name (username): ')
        password1 = input('Enter password: ')
        allusers = User.select().where(User.username == username1).limit(1)
        if len(allusers) != 1:
            print("Error")
        user = allusers[0]
        if user.username == username1:
            if user.password == password1:
                print('Hi, ', username1)
                print(user.username, user.password)
                return True
            else:
                print('User or password incorrect!')
                return False
        return False

    @classmethod
    def user_interface(cls):
        print("User Interface")
        action = input("Enter number from 1 to 5")
        return action

