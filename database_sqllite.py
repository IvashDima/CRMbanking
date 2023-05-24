import sqlite3
import datetime

# Core Functionality
# with sqlite3.connect('db/database.db') as db:
#     cursor = db.cursor()
#     # query = """ CREATE TABLE IF NOT EXISTS contacts(id INTEGER, name TEXT) """
#     query1 = """ INSERT INTO contacts (id, name) VALUES (1, 'Dmytro')  """
#     query2 = """ INSERT INTO contacts (name, id) VALUES ('Iryna', 2)  """
#     query3 = """ INSERT INTO contacts VALUES (3, 'Pavlo')  """
#     cursor.execute(query1)
#     cursor.execute(query2)
#     cursor.execute(query3)
# Some logic. Classe, Functions
#     # db.commit()

def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

# insert_contracts = [
# #     (1, 5000, get_timestamp(2023,5,18), 1),
# #     (2, 5000, get_timestamp(2023,5,18), 2),
# #     (3, 5000, get_timestamp(2023,5,18), 3),
# #     (4, 5000, get_timestamp(2023,5,18), 1),
# #     (5, 5000, get_timestamp(2023,5,18), 1),
# #     (6, 5000, get_timestamp(2023,5,18), 2)
#     (7, 5000, get_timestamp(), 1)
#     (8, 5000, get_timestamp(datetime.datetime.now()), 1)

# ]

# with sqlite3.connect('db/database.db') as db:
#     cursor = db.cursor()
# #     # query = """ CREATE TABLE IF NOT EXISTS contracts(
# #     #     id INTEGER,
# #     #     amount REAL,
# #     #     start_date INTEGER,
# #     #     contact_id INTEGER
# #     # ) """
#     query = """ INSERT INTO contracts (id, amount, start_date, contact_id) VALUES(?, ?, ?, ?)  """
#     # query1 = """ INSERT INTO contacts (id, name) VALUES (1, 'Dmytro')  """
#     # query2 = """ INSERT INTO contacts (name, id) VALUES ('Iryna', 2)  """
#     # query3 = """ INSERT INTO contacts VALUES (3, 'Pavlo')  """
#     cursor.executemany(query, insert_contracts)
#     db.commit()
#     print(cursor.rowcount, " row added")

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """ SELECT contracts.amount, contracts.start_date, contacts.name  FROM contracts JOIN contacts
                ON contacts.id = contracts.contact_id 
                WHERE (start_date > %(from)d)
                AND (start_date < %(to)d)
                """ % {'from': get_timestamp(2023,5,19), 'to': get_timestamp(2023,5,25)}
                # contact_id = 1
    cursor.execute(query)
    sum = 0
    for res in cursor:
        sum += res[0]
        print(res[0], get_date(res[1]), res[2])
    print('TOTAL', sum)