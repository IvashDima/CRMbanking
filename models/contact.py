from models.basemodel import *

class Contact(BaseModel):
    name = CharField(max_length=50)
    email = CharField(max_length=20)

    # def __init__(self, name: str, email: str, id, created, *args, **kwargs):
    #     super().__init__(id, created, *args, **kwargs)
    #     self.email = email
    #     self.name = name

    class Meta:
        db_table = 'contacts'


class Cont:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

    def __str__(self):
        return f"Name is {self.__name}, call to {self.__phone}"

    # con1 = Cont('Dmytro', '1111')
    # print(con1)

