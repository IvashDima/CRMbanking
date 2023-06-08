from models.contact import create_contact
from logs.config import logger


def import_contact(file_name):
    with open(file_name, "r") as file:
        header = file.readline()
        for line in file:
            name1, email1, age1, gender_answer = line.strip().split(",")
            # print(name1, email1, age1, gender_answer)
            msg = create_contact(name=name1, email=email1, age=int(age1), gender=gender_answer)
            logger.info("Imported row: " + str(msg))
        text = "Import completed!"
    return text
