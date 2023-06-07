from models.basemodel import *


def create_contact(name, email, age, gender):
    contact = Contact.select().where(Contact.name == name).limit(1)
    if len(contact) >= 1:
        text = f'Contact with name "{name}" exist!'
    else:
        contact = Contact(name=name, email=email, age=age, gender=gender).save()
        text = f'Contact with name "{name}" successfully created!'
    return text


def get_contact():
    contacts = Contact.select(Contact.id, Contact.created, Contact.name, Contact.email, Contact.age, Contact.gender)
    if len(contacts) >= 1:
        return contacts
    else:
        text = f'Contacts not found!'
        return text


class Gender(BaseModel):
    name = CharField()

    def __init__(self, name: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    class Meta:
        db_table = 'genders'


class Contact(BaseModel):
    name = CharField(max_length=50)
    age = IntegerField()
    gender_id = ForeignKeyField(Gender)
    email = CharField(max_length=20)

    def __init__(self, name: str, email: str, age: int, gender=Gender, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gender = gender
        self.age = age
        self.email = email
        self.name = name

    def __str__(self):
        return f"{self.id} {self.created} {self.name} {self.email} {self.age} {self.gender}"

    class Meta:
        db_table = 'contacts'