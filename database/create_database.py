from models.user import User, create_user
from models.contact import Contact, Gender
from models.lead import Lead
from models.contract import Contract
from models.product import Product
from database.database import DB


def create_db():

    with DB:
        # create_tables
        DB.create_tables([User, Lead, Contact, Contract, Product, Gender])  # create_db

        # test data
        create_user(username='test', password='test')       # test user
        gender_m = Gender(name='Male')
        gender_f = Gender(name='Female')