from models.user import create_user
from models.gender import Gender
from database.database import DB


male = 'Male'
female = 'Female'

# gender_m = ()
# gender_f = ()

with DB:

    # test data
    create_user(username='test', password='test')

    gender_m = Gender.select().where(Gender.name == male).limit(1)
    if len(gender_m) == 0:
        gender_m = Gender(name=male).save()

    gender_f = Gender.select().where(Gender.name == female).limit(1)
    if len(gender_f) == 0:
        gender_f = Gender(name=female).save()