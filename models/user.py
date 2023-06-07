from models.basemodel import *


def create_user(username, password):
    # try:
    #     user = User.select().where(User.username == username).get()
    # except (KeyError, NameError) as e:
    #     print(e)
    user = User.select().where(User.username == username).limit(1)
    if len(user) >= 1:
        text = f'User with username "{username}" exist!'
    else:
        user = User(username=username, password=password).save()
        text = f'User with username "{username}" successfully created!'
    return text


# noinspection LanguageDetectionInspection
def get_users():
    allusers = User.select()
    if len(allusers) >= 1:
        return allusers
    else:
        text = f'Users not found!'
        return text


class User(BaseModel):
    username = CharField(max_length=50)
    password = CharField(max_length=20)

    def __init__(self, username: str, password: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = password
        self.username = username

    def __str__(self):
        return f"{self.id} {self.created} {self.username} {self.password}"

    class Meta:
        db_table = 'users'
