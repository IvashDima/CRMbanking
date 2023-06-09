from models.contact import get_contact
from src.date_format import currentdatetime_str
from logs.config import logger


def export_contact():
    file_name = f"contacts_data_{currentdatetime_str}.csv"
    with open(file_name, "w") as file:
        msgs = get_contact()
        if isinstance(msgs, list):
            file.write("name," + "email," + "age," + "gender" + "\n")
            # print("Header done!")
            for msg in msgs:
                file.write(msg.name + "," + msg.email + "," + str(msg.age) + "," + msg.gender_id.name + "\n")
                # print(msg)
                logger.info("Exported row: " + str(msg))
            text = "Export completed!"
        else:
            # print(msgs)
            text = msgs
    return text, file_name




