import requests

from configuration import AGE_URL, GENDER_URL

class AgeByName:
    def __init__(self, name, age, count):
        self.name = name
        self.age = age
        self.count = count

    def __str__(self):
        return f"{self.name} {self.age} {self.count}"


def get_age_by_name(income_name):
    URL = AGE_URL + income_name
    response = requests.get(url=URL)
    received_data = response.json()
    print(URL)
    print(received_data)
    # {'age': 40, 'count': 10048, 'name': 'Dima'}
    if 200 <= response.status_code <= 299:
        received_data = response.json()
        print(received_data)
        age1 = AgeByName(name=received_data["name"], age=received_data["age"], count=received_data["count"])
        print(f"Check age: {income_name}'s average age is {age1.age}.")
    elif 400 <= response.status_code <= 499:
        if response.status_code == 401:
            print(f"Error: {response.status_code} - Unautherized. Error text: Invalid API key")
        elif response.status_code == 402:
            print(f"Error: {response.status_code} - Payment Required. Error text: Subscription is not active")
        elif response.status_code == 422:
            print(f"Error: {response.status_code} - Unprocessable Entity. Error text: Missing 'name' parameter")
        elif response.status_code == 429:
            print(f"Error: {response.status_code} - Too Many Requests. Error text: Request limit reached")
        else:
            print(f"Error: {response.status_code}")
    else:
        print(f"Other error: {response.status_code}")


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
    response = requests.get(url=URL)
    if 200 <= response.status_code <= 299:
        received_data = response.json()
        print(received_data)
        gender1 = GenderByName(name=received_data["name"], gender=received_data["gender"],
                               probability=received_data["probability"], count=received_data["count"])
        print(f"Check gender: {income_name}'s gender is '{gender1.gender}' with probability = {gender1.probability} ")
    elif 400 <= response.status_code <= 499:
        if response.status_code == 401:
            print(f"Error: {response.status_code} - Unautherized. Error text: Invalid API key")
        elif response.status_code == 402:
            print(f"Error: {response.status_code} - Payment Required. Error text: Subscription is not active")
        elif response.status_code == 422:
            print(f"Error: {response.status_code} - Unprocessable Entity. Error text: Missing 'name' parameter")
        elif response.status_code == 429:
            print(f"Error: {response.status_code} - Too Many Requests. Error text: Request limit reached")
        else:
            print(f"Error: {response.status_code}")
    else:
        print(f"Other error: {response.status_code}")


