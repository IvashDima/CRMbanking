from src.date_format import currentdate
from database.database import DB
from peewee import *


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    created = DateTimeField(default=currentdate)
    # modified = DateTimeField(default=datetime.datetime.timestamp())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        database = DB
        order_by = ('created', 'id')
