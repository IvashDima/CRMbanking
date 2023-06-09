from models.user import create_user
from models.gender import Gender
from models.product import Product
from database.database import DB

male = 'Male'
female = 'Female'

loan = 'Loan'
deposit = 'Deposit'


def create_base_data():
    with DB:
        # test data
        create_user(username='test', password='test')

        gender_m = Gender.select().where(Gender.name == male).limit(1)
        if len(gender_m) == 0:
            gender_m = Gender(name=male).save()

        gender_f = Gender.select().where(Gender.name == female).limit(1)
        if len(gender_f) == 0:
            gender_f = Gender(name=female).save()

        loan_product = Product.select().where(Product.name == loan).limit(1)
        if len(loan_product) == 0:
            loan_product = Product(name=loan).save()

        deposit_product = Product.select().where(Product.name == deposit).limit(1)
        if len(deposit_product) == 0:
            deposit_product = Product(name=deposit).save()
    return gender_m, gender_f, loan_product, deposit_product


gender_m = Gender.select().where(Gender.name == male).limit(1)
gender_f = Gender.select().where(Gender.name == female).limit(1)
loan_product = Product.select().where(Product.name == loan).limit(1)
deposit_product = Product.select().where(Product.name == deposit).limit(1)