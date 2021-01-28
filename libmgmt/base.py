from abc import ABC, ABCMeta
from libmgmt.status import UserStatus, AccountStatus

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

class Account(metaclass=ABCMeta):
    def __init__(self, id, password, person,
                 user_status=UserStatus.ANONYMOUS, status=AccountStatus.ACTIVE):
        self.__id = id,
        self.__password = password
        self.__person = person
        self.__status = status
        self.__user_status = user_status

    def user_login_check(func):
        def wrap(self, *args, **kwargs):
            if self.__user_status != UserStatus.LOGGED_IN:
                print("User Not Authorized! to perform this action")
            else:
                return func(self, *args, **kwargs)
        return wrap

    def register(self):
        #not using in my example
        pass

    def login(self, password):
        if self.__password == password:
            self.__user_status = UserStatus.LOGGED_IN
            print(f"{self.__person.name}, user logged in!!!")
        else:
            print("Username and password doesn't match!")

    @user_login_check
    def logout(self):
        self.__user_status = UserStatus.ANONYMOUS
        print(f"{self.name} logged out")

    @property
    def name(self):
        return self.__person.name

class Book(ABC):
    def __init__(self, title, subject, publisher,
                 language, author, number_of_pages):
        self.__title = title
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__author = author
        self.__number_of_pages = number_of_pages

