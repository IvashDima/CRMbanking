from models.basemodel import *
from models.contact import *
from models.product import *


class Contract(BaseModel):
    amount = FloatField()
    start_date = DateField()
    contact_id = ForeignKeyField(Contact)
    product_id = ForeignKeyField(Product)

    # def __init__(self, amount: int, start_date, contact_id: Contact, product_id: Product, id, created, *args, **kwargs):
    #     super().__init__(id, created, *args, **kwargs)
    #     self.product_id = product_id
    #     self.contact_id = contact_id
    #     self.start_date = start_date.strftime("%d.%m.%Y")
    #     self.amount = amount

    class Meta:
        db_table = 'contracts'
