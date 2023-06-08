from models.contact import get_contact
import datetime

def export_contact():
    currentdate = str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    file_name = f"contacts_data_{currentdate}.csv"
    with open(file_name, "w") as file:
        msgs = get_contact()
        if isinstance(msgs, list):
            file.write("name," + "email," + "age," + "gender" + "\n")
            # print("Header done!")
            for msg in msgs:
                file.write(msg.name + "," + msg.email + "," + str(msg.age) + "," + msg.gender_id.name + "\n")
                # print(msg)
            text = "Export completed!"
        else:
            # print(msgs)
            text = msgs
    return text, file_name




