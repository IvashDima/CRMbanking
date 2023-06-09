from models.basemodel import *
from models.contact import Contact
from models.product import Product

from src.date_format import currentdate

from checks.public_data.data_by_name import get_gender_by_name, get_age_by_name


def create_contract(amount, contact_id, product_id):
    contacts = Contact.select().where(Contact.id == contact_id).limit(1)
    for contact in contacts:
        print(get_age_by_name(contact.name))
        print(get_gender_by_name(contact.name))
    contract = Contract.select().where(Contract.contact_id == contact_id and
                                       Contract.product_id == product_id).limit(1)
    if len(contract) >= 1:
        text = f'Contract for Contact_id={contact_id} with Product_id={product_id} exist!'
    else:
        contract = Contract(amount=amount, contact_id=contact_id, product_id=product_id).save()
        text = f'Contract for Contact_id={contact_id} with Product_id={product_id} successfully created!'
    return text


def get_contract():
    contracts = Contract.select()
    if len(contracts) >= 1:
        text = []
        for contract in contracts:
            text.append(contract)
        return text
    else:
        text = f'Contracts not found!'
        return text


class Contract(BaseModel):
    amount = FloatField()
    start_date = DateField(default=currentdate)
    contact_id = ForeignKeyField(Contact)
    product_id = ForeignKeyField(Product)

    def __init__(self, amount: int, contact_id=Contact, product_id=Product, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.product_id = product_id
        self.contact_id = contact_id
        self.amount = amount

    def __str__(self):
        return f"{self.id} {self.created} {self.amount} {self.start_date} {self.contact_id.name} {self.product_id.name}"

    class Meta:
        db_table = 'contracts'
