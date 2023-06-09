import requests

from configuration import AGE_URL, GENDER_URL
from logs.config import logger
from src.errors.api_errors import UNAUTHERIZED, PAYMENT_REQUIRED, UNPROCESSABLE_ENTITY, TOO_MANY_REQUESTS


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
    elif 400 <= response.status_code <= 499:
        if response.status_code == 401:
            text = UNAUTHERIZED
            logger.error(f"{for_logger} {UNAUTHERIZED}")
        elif response.status_code == 402:
            text = PAYMENT_REQUIRED
            logger.error(f"{for_logger} {PAYMENT_REQUIRED}")
        elif response.status_code == 422:
            text = UNPROCESSABLE_ENTITY
            logger.error(f"{for_logger} {UNPROCESSABLE_ENTITY}")
        elif response.status_code == 429:
            text = TOO_MANY_REQUESTS
            logger.error(f"{for_logger} {TOO_MANY_REQUESTS}")
        else:
            text = f"Error: {response.status_code}"
            logger.error(f"{for_logger} Error: {response.status_code} ")
    else:
        text = f"Other error: {response.status_code}"
        logger.error(f"{for_logger} Other error: {response.status_code} ")
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
    elif 400 <= response.status_code <= 499:
        if response.status_code == 401:
            text = UNAUTHERIZED
            logger.error(f"{for_logger} {UNAUTHERIZED}")
        elif response.status_code == 402:
            text = PAYMENT_REQUIRED
            logger.error(f"{for_logger} {PAYMENT_REQUIRED}")
        elif response.status_code == 422:
            text = UNPROCESSABLE_ENTITY
            logger.error(f"{for_logger} {UNPROCESSABLE_ENTITY}")
        elif response.status_code == 429:
            text = TOO_MANY_REQUESTS
            logger.error(f"{for_logger} {TOO_MANY_REQUESTS}")
        else:
            text = f"Error: {response.status_code}"
            logger.error(f"{for_logger} Error: {response.status_code} ")
    else:
        text = f"Other error: {response.status_code}"
        logger.error(f"{for_logger} Other error: {response.status_code} ")
    return text