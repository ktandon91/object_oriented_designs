from libmgmt.base import Account

from libmgmt.mixins import GenrealBookOperationsMixin, AccountOperationsMixin,\
    MemberOperationsMixin, SpecialAdminBookOperationsMixin



class Librarian(GenrealBookOperationsMixin, SpecialAdminBookOperationsMixin,
                AccountOperationsMixin, MemberOperationsMixin, Account):
    def __init__(self, id, password, person):
        super().__init__(id, password, person)



class Member(Account, GenrealBookOperationsMixin, AccountOperationsMixin):
    def __init__(self, id, password, person):
        super().__init__(id, password, person)

    @Account.user_login_check
    def reserve_book(self):
        super().reserve_book("book")
        print(f"{self.name} is reserving a book")

    @property
    def name(self):
        return super().name




