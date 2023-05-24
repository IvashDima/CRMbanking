# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from models.user import *
from models.lead import *
from models.contact import *
from models.contract import *
from models.product import *

import datetime
from peewee import *
# from models.create_database import *

# from models.action import *

def print_hi(name):
    print(f'Hi, {name}')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Welcome to CRMBanking')
    # Core Functionality
    # if UserAction.login_user() == True:
    #     print("User is logged in")
    #     action = UserAction.user_interface()
        # if action == '1':
            # Create contract
        # elif action == '2':
            # Delete Contract
    with DB:
    ## create_tables
        DB.create_tables([User, Lead, Contact, Contract, Product])
        # create lead
        # amount1 = input('Enter amount: ')
        # contact_id1 = input('Enter contact_id: ')
        # lead1 = Lead(amount=amount1,contact_id=contact_id1).save()
        # print(lead1)


        # username1 = input('Enter your name (username): ')
        # password1 = input('Enter password: ')
        # allusers = User.select().where(User.username == username1).limit(1)
        # if len(allusers) != 1:
        #     print("Error")
        # user = allusers[0]
        # if user.username == username1:
        #     if user.password == password1:
        #         print_hi(username1)
        #         print(user.username, user.password)
        #     else:
        #         print('User or password incorrect!')

        ## create user
        username1 = input('Enter username: ')
        password1 = input('Enter password: ')

        user1 = create_user(username=username1, password=password1)
        print(user1)

    # insert_data
    # Dmytro = Contact(name='Dima').save()
    # Iryna = Contact.create(name='Ira')
    # Pavlo = Contact.insert(name='Pasha').save()
    # contacts = Contact.select()
    # insert_many
    # contracts = [
    #     Contact{'amount'=13, 'start_date'=datetime.date(2023,5,13), 'contact_id':contacts[0]},
    #     {'amount':14, 'start_date':datetime.date(2023,5,14), 'contact_id':contacts[1]},
    # ]
    # Contract.insert_many(contracts).execute()
    # select
    # contacts = Contact.select().where(Contact.id == 2)
    # print(contacts[0])
    # get
    # contacts = Contact.get(Contact.id == 2)
    # print(contacts.id, contacts.name)
    # join
    # allcontracts = Contract.select().join(Contact).where(Contact.id == 2)
#     allcontracts = Contract.select().where(Contract.contact_id == 2)
#     print(len(allcontracts))
#     print(allcontracts)
#     print(type(allcontracts))
#     for contr in allcontracts:
#         print(contr.amount, contr.start_date, contr.contact_id.name)
    print('DONE')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
