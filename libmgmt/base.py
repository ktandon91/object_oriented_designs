from abc import ABC

class Person(ABC):
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

    @property
    def name(self):
        return self.__name

class Address(ABC):
    def __init__(self, street="main street", city="New Delhi", state="Delhi", zip_code=110064):
        self.__street = street
        self.__city = city
        self.__city = state
        self.__zip_code = zip_code