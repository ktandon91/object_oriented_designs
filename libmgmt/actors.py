from abc import ABC, abstractmethod
from libmgmt.status import AccountStatus, UserStatus

class Account(ABC):
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
                raise Exception("User Not Authorized! to perform this action")
            else:
                return func(self, *args, **kwargs)
        return wrap

    def reset_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password


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

class Librarian(Account):
    def __init__(self, id, password, person):
        super().__init__(id, password, person)

    def add_book(self):
        pass

    def block_member(self, member):
        pass

    def un_block_member(self, member):
        pass

class Member(Account):
    def __init__(self, id, password, person):
        super().__init__(id, password, person)

    @Account.user_login_check
    def reserve_book(self):
        print(f"{self.name} is reserving a book")

    @property
    def name(self):
        return super().name




