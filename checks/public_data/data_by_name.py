import requests

from configuration import AGE_URL, GENDER_URL
from logs.config import logger
from src.errors.api_errors import UNAUTHERIZED, PAYMENT_REQUIRED, UNPROCESSABLE_ENTITY, TOO_MANY_REQUESTS


def error_handling(error_code, text_for_logger):
    if 400 <= error_code <= 499:
        if error_code == 401:
            text = UNAUTHERIZED
            logger.error(f"{text_for_logger} {UNAUTHERIZED}")
        elif error_code == 402:
            text = PAYMENT_REQUIRED
            logger.error(f"{text_for_logger} {PAYMENT_REQUIRED}")
        elif error_code == 422:
            text = UNPROCESSABLE_ENTITY
            logger.error(f"{text_for_logger} {UNPROCESSABLE_ENTITY}")
        elif error_code == 429:
            text = TOO_MANY_REQUESTS
            logger.error(f"{text_for_logger} {TOO_MANY_REQUESTS}")
        else:
            text = f"Error: {error_code}"
            logger.error(f"{text_for_logger} {text}")
    else:
        text = f"Other error: {error_code}"
        logger.error(f"{text_for_logger} {text}")
    return text


class AgeByName:
    def __init__(self, name, age, count):
        self.name = name
        self.age = age
        self.count = count

    def __str__(self):
        return f"{self.name} {self.age} {self.count}"


def get_age_by_name(income_name):
    URL = AGE_URL + income_name
    for_logger = f"get_age_by_name for {income_name}."
    response = requests.get(url=URL)
    if 200 <= response.status_code <= 299:
        received_data = response.json()
        logger.info(f"{for_logger} returned: {received_data}.")
        age1 = AgeByName(name=received_data["name"], age=received_data["age"], count=received_data["count"])
        text = f"Check age: {income_name}'s average age is {age1.age}."
    else:
        text = error_handling(response.status_code, for_logger)
    return text


class GenderByName:
    def __init__(self, name: str, gender: str, probability: float, count: int):
        self.name = name
        self.gender = gender
        self.probability = probability
        self.count = count

    def __str__(self):
        return f"{self.name} {self.gender} {self.probability} {self.count}"


def get_gender_by_name(income_name):
    URL = GENDER_URL + income_name
    for_logger = f"get_gender_by_name for {income_name}."
    response = requests.get(url=URL)
    if 200 <= response.status_code <= 299:
        received_data = response.json()
        logger.info(f"{for_logger} returned: {received_data}.")
        gender1 = GenderByName(name=received_data["name"], gender=received_data["gender"],
                               probability=received_data["probability"], count=received_data["count"])
        text = f"Check gender: {income_name}'s gender is '{gender1.gender}' with probability = {gender1.probability}"
    else:
        text = error_handling(response.status_code, for_logger)
    return text


print(get_gender_by_name('Katya'))
print(get_age_by_name('Katya'))
