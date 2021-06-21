from parking_lot.types_and_status import VehicleType, UserLoginStatus
from abc import ABC, abstractmethod

class Location:
    def __init__(self, street="street", city="Delhi",
                 state='Delhi', pincode=110064):
        self._street = street
        self._city = city
        self._state = state
        self._pincode = pincode

class Person:
    def __init__(self, name, address, email, phone):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone

class Account:
    def __init__(self, person, username, password):
        self._person = person
        self._username = username
        self._password = password
        self._user_status = UserLoginStatus.ANONYMOUS

    def user_login_check(func):
        def wrap(self, *args, **kwargs):
            if self._user_status != UserLoginStatus.LOGGED_IN:
                print("User not authorized!! for this functionality")
            else:
                func(self, *args, **kwargs)

    def register(self):
        pass

    def login(self):
        pass

    def logout(self):
        pass


class Vehicle(ABC):
    def __init__(self, licensenumber, type=VehicleType.LMV):
        self._licensenumber = licensenumber
        self._type = type

    @abstractmethod
    def assign_ticket(self):
        pass