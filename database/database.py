from peewee import *

# Set DataBase
DATABASE_NAME = 'database/database.db'
db_sqlite = SqliteDatabase(DATABASE_NAME)
db_mysql = MySQLDatabase('mysql_db',user='db_user',passqord='db_pass',host='localhost')
db_postgresql = PostgresqlDatabase('mysql_db',user='db_user',password='db_pass',host='localhost')

    # if Something:
    #     database = db
    # elif Something2:
    #     database = db_my
    # else:
    #     database = db_post
DB = db_sqlite