# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from user_interface.consol_action import UserAction
from database.create_database import create_db


def menu_main():

    def menu_operation():
        while True:
            action = UserAction.operation()
            if action == '0':
                raise SystemExit
            elif action == '9':
                break
            else:
                print("Incorrect operation")

    def menu_contact():
        while True:
            action = UserAction.operation()
            if action == '0':
                raise SystemExit
            elif action == '1':
                UserAction.operation_create_contact()
            elif action == '2':
                UserAction.operation_get_contact()
            elif action == '9':
                break
            else:
                print("Incorrect operation")

    def menu_user():
        while True:
            action = UserAction.operation()
            if action == '0':
                raise SystemExit
            elif action == '1':
                UserAction.operation_create_user()
            elif action == '2':
                UserAction.operation_get_user()
            elif action == '9':
                break
            else:
                print("Incorrect operation")

    while True:
        action = UserAction.section()
        if action == '0':
            raise SystemExit
        elif action == '1':     # Contacts
            menu_contact()
        elif action == '2':     # Contracts
            menu_operation()
        elif action == '3':     # Leads
            menu_operation()
        elif action == '4':     # Users
            menu_user()
        elif action == '5':     # Products
            menu_operation()
        else:
            print("Incorrect section")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Core Functionality
    create_db()

    if UserAction.login_user():
        menu_main()

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
    print('End of program')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
