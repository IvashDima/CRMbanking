from models.basemodel import *


def create_user(username, password):
    # try:
    #     user = User.select().where(User.username == username).get()
    # except KeyError as e:
    #     print(f'User with username {username} exist!')
    # else:
    user = User(username=username, password=password).save()
    print(f'User with username {username} successfully created!', user)


class User(BaseModel):
    username = CharField(max_length=50)
    password = CharField(max_length=20)

    def __init__(self, username: str, password: str, id, created, *args, **kwargs):
        super().__init__(id, created, *args, **kwargs)
        self.__username = username
        self.password = password

    class Meta:
        db_table = 'users'

