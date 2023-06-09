from models.basemodel import *


class Product(BaseModel):
    name = CharField(max_length=100)

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        return f"{self.id} {self.created} {self.name}"

    class Meta:
        db_table = 'products'