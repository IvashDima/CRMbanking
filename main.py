# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from user_interface.consol_action import *
from database.create_database import DB

# test changes

class Menu:
    def menu(self, action):
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


# class Section(Menu):
def menu_sections():    # (self, action):
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Core Functionality
    with DB:
        # create_tables
        DB.create_tables([User, Lead, Contact, Contract, Product]) # create_db
        if UserAction.login_user() == True:
            menu_sections()

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
    # contracts = Contract.select().join(Contact).where(Contact.id == 2)
#     contracts = Contract.select().where(Contract.contact_id == 2)
#     print(len(contracts))
#     print(contracts)
#     print(type(contracts))
#     for cont in contracts:
#         print(cont.amount, cont.start_date, cont.contact_id.name)
    print('DONE')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
