# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from models.user import *
from models.lead import *
from models.contact import *
from models.contract import *
from models.product import *
from models.consol_action import *

import datetime
from peewee import *
# from models.create_database import *

# from models.action import *

def menu_operation(section):
    while True:
        action = UserAction.operation()
        if action == '1':
            if section == 'Contacts':
                print("TBD")
            elif section == 'Contracts':
                print("TBD")
            elif section == 'Leads':
                print("TBD")
            elif section == 'Users':
                UserAction.operation_create_user()
            elif section == 'Products':
                print("TBD")
            else:
                print("Incorrect section")
        elif action == '2':
            if section == 'Contacts':
                print("TBD")
            elif section == 'Contracts':
                print("TBD")
            elif section == 'Leads':
                print("TBD")
            elif section == 'Users':
                UserAction.operation_get_user()
            elif section == 'Products':
                print("TBD")
            else:
                print("Incorrect section")
        elif action == '9':
            break
        elif action == '0':
            raise SystemExit
        else:
            print("Incorrect answer")
def menu_section():
    while True:
        action = UserAction.section()
        if action == '1':
            menu_operation('Contacts')
        elif action == '2':
            menu_operation('Contracts')
        elif action == '3':
            menu_operation('Leads')
        elif action == '4':
            menu_operation('Users')
        elif action == '5':
            menu_operation('Products')
        elif action == '0':
            raise SystemExit
        else:
            print("Incorrect answer")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Core Functionality
    if UserAction.login_user() == True:
        menu_section()

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
