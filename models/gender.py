from models.basemodel import *


class Gender(BaseModel):
    name = CharField()
    # male = "Male"
    # female = "Female"

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    class Meta:
        db_table = 'genders'
