from libmgmt.base import Account


class MetaLoginCheck(type):
    def __new__(cls, name, bases, local):
        for attr in local:
            if callable(attr):
                local[attr] = Account.user_login_check(local[attr])
        return type.__new__(cls, name, bases, local)

class GenrealBookOperationsMixin:

    __metaclass__ = MetaLoginCheck

    def reserve_book(self, book):
        pass

    def renew_book(self, book):
        pass

    def return_book(self, book):
        pass

    def remove_reservation(self, book):
        pass

class AccountOperationsMixin:

    __metaclass__ = MetaLoginCheck

    def reset_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password

    def view_account(self):
        pass

class MembershipOperationsMixin:

    __metaclass__ = MetaLoginCheck

    def cancel_membership(self):
        pass

class MemberOperationsMixin:

    __metaclass__ = MetaLoginCheck

    def block_member(self, member):
        pass

    def un_block_member(self, member):
        pass

class SpecialAdminBookOperationsMixin:

    __metaclass__ = MetaLoginCheck

    def issue_book(self):
        pass

    def edit_book(self):
        pass

    def add_book(self):
        pass


