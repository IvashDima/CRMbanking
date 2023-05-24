from models.basemodel import *

class Product(BaseModel):
    name = CharField(max_length=100)

    # def __init__(self, name: str, id, created, *args, **kwargs):
    #     super().__init__(id, created, *args, **kwargs)
    #     self.name = name

    class Meta:
        db_table = 'products'