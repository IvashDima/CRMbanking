from models.user import create_user, get_users, User
from models.contact import create_contact, get_contact
from models.contract import create_contract, get_contract
# from models.lead import *
# from models.product import *

from file_io.import_data import import_contact
from file_io.export_data import export_contact

from logs.config import logger


class UserAction:
    @classmethod
    def login_user(cls):
        print('Welcome to CRMBanking')
        username_in = input('Enter your name (username): ')
        password_in = input('Enter password: ')
        allusers = User.select().where(User.username == username_in).limit(1)
        if len(allusers) != 1:
            print("User or password incorrect!")
        user = allusers[0]
        if user.username == username_in:
            if user.password == password_in:
                print('Hi, ', username_in)
                logger.info(f"User {username_in} is logged in")
                return True
            else:
                print('User or password incorrect!')
                return False
        return False

    @classmethod
    def section(cls, user_role):
        section_config = {
            'Admin': {1: 'Contacts', 2: 'Contracts', 3: 'Leads', 4: 'Users', 5: 'Products', 0: 'Exit'},
            'Manager': {1: 'Contacts', 2: 'Contracts', 3: 'Leads', 5: 'Products', 0: 'Exit'},
        }
        section = section_config[user_role]
        print("Choose section!")
        for point, option in section.items():
            print(f"{point} - {option}")
        action = input(f"Your choose: ")
        return action

    @classmethod
    def operation(cls, section):
        operation_config = {
            'Contacts': {1: 'Create contact', 2: 'Get Info', 3: 'Import from file', 4: 'Export in file',
                         9: 'Go to Section', 0: 'Exit'},
            'Contracts': {1: 'Create contract', 2: 'Get Info', 9: 'Go to Section', 0: 'Exit'},
            'Leads': {9: 'Go to Section', 0: 'Exit'},
            'Users': {1: 'Create contact', 2: 'Get Info', 9: 'Go to Section', 0: 'Exit'},
            'Products': {9: 'Go to Section', 0: 'Exit'}
        }
        operation = operation_config[section]
        print("Choose operation!")
        for point, option in operation.items():
            print(f"{point} - {option}")
        action = input(f"Your choose: ")
        return action

    @classmethod
    def operation_create_user(cls):
        username_in = input('Enter username: ')
        password_in = input('Enter password: ')
        msg = create_user(username=username_in, password=password_in)
        return print(msg)

    @classmethod
    def operation_get_user(cls):
        msgs = get_users()
        if isinstance(msgs, list):
            print("All users (Id, Created, Username, Password):")
            for msg in msgs:
                print(msg)
        else:
            print(msgs)

    @classmethod
    def operation_create_contact(cls):
        msg = ''
        name_in = input('Enter name: ')
        email_in = input('Enter E-mail: ')
        age_in = input('Enter age: ')
        gender_answer_in = input('Enter gender (m - male, f - female): ')
        msg = create_contact(name=name_in, email=email_in, age=age_in, gender=gender_answer_in)
        return print(msg)

    @classmethod
    def operation_get_contact(cls):
        msgs = get_contact()
        if isinstance(msgs, list):
            print("All contacts (Id, Created, Name, E-Mail, Age, Gender):")
            for msg in msgs:
                print(msg)
        else:
            print(msgs)

    @classmethod
    def operation_import_contact(cls):
        msg = ''
        print("To import contacts data need to enter a file path (a list of directory names concatenated "
              "by a directory separator) and a file name.")
        print("Format: '*.csv'. Example: ")
        print("Linux, MacOS:    /home/peter/PycharmProjects/data_file.csv")
        print("Windows:    C:\Documents\Peter\PycharmProjects\data_file.csv")
        print("Structure inside file: ")
        print("Header: 'name, email, age, gender'")
        print("Line1: 'Dmytro, d@x.com, 30, m'")
        print("Line1: 'Olga, o@x.com, 35, f'")
        file_name_in = input('Enter a file path: ')
        msg = import_contact(file_name=file_name_in)
        return print(msg)

    @classmethod
    def operation_export_contact(cls):
        msg = ''
        msg, file_name = export_contact()
        print(msg)
        return print(f"Exported file is located in the root folder of the application with name: {file_name}.")

    @classmethod
    def operation_create_contract(cls):
        msg = ''
        amount_in = input('Enter amount of contract: ')
        contact_id_in = input('Enter contact_id: ')
        product_id_in = input('Enter product_id (1 - Loan, 2 - Deposit): ')
        msg = create_contract(amount=amount_in, contact_id=contact_id_in, product_id=product_id_in)
        return print(msg)

    @classmethod
    def operation_get_contract(cls):
        msgs = get_contract()
        if isinstance(msgs, list):
            print("All contracts (Id, Created, Amount, Start date, Contact, Product):")
            for msg in msgs:
                print(msg)
        else:
            print(msgs)


    # create lead
    # amount1 = input('Enter amount: ')
    # contact_id1 = input('Enter contact_id: ')
    # lead1 = Lead(amount=amount1,contact_id=contact_id1).save()
    # print(lead1)
