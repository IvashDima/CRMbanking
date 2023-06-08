from models.contact import create_contact


def import_contact(file_name):
    file = open(file_name, "r")
    header = file.readline()
    for line in file:
        name1, email1, age1, gender_answer = line.strip().split(",")
        print(name1, email1, age1, gender_answer)
        msg = create_contact(name=name1, email=email1, age=int(age1), gender=gender_answer)
        print(msg)
    file.close()
    return "Import completed!"
