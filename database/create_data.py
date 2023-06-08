from models.user import create_user
from models.gender import Gender
from database.database import DB


# gender_m =
# gender_f = []

with DB:

    # test data
    create_user(username='test', password='test')       # test user
    gender_m = Gender(name='Male').save()
    gender_f = Gender(name='Female').save()