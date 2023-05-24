from models.basemodel import *


def create_user(username, password):
    # try:
    #     user = User.select().where(User.username == username).get()
    # except (KeyError, NameError) as e:
    #     print(e)
    user = User.select().where(User.username == username).limit(1)
    if len(user) >= 1:
        print(f'User with username "{username}" exist!')
    else:
        user = User(username=username, password=password).save()
        print(f'User with username "{username}" successfully created!')


class User(BaseModel):
    username = CharField(max_length=50)
    password = CharField(max_length=20)

    # def __init__(self, username: str, password: str, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__username = username
    #     self.password = password

    class Meta:
        db_table = 'users'
