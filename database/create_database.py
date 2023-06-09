from models.user import User, create_user
from models.contact import Contact
from models.gender import Gender
from models.lead import Lead
from models.contract import Contract
from models.product import Product
from database.database import DB


def create_db():
    with DB:
        # create_tables
        DB.create_tables([User, Lead, Contact, Contract, Product, Gender])