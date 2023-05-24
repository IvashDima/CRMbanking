from faker import Faker

from models.database import *
from models.user import *
from models.lead import *
from models.contact import *
from models.contract import *
from models.product import *

def create_db(load_fake_data: bool = True):

    with DB:
        # create_tables
        DB.create_tables([User, Lead, Contact, Contract, Product])
