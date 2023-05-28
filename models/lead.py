from models.basemodel import *
from models.contact import *


class Lead(BaseModel):
    amount = FloatField()
    contact_id = ForeignKeyField(Contact)

    # def __init__(self, amount: int, contact_id: Contact, id, created, *args, **kwargs):
    #     super().__init__(id, created, *args, **kwargs)
    #     self.contact_id = contact_id
    #     self.amount = amount

    class Meta:
        db_table = 'leads'
