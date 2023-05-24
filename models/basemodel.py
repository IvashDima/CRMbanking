import datetime
from models.database import *
from peewee import *

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    created = DateTimeField(default=datetime.datetime.now())
    # modified = DateTimeField(default=datetime.datetime.timestamp())

    def __init__(self, id, created, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created = created.strftime("%d.%m.%Y %H:%M:%S")
        self.id = id

    class Meta:
        database = DB
        order_by = ('created', 'id')
