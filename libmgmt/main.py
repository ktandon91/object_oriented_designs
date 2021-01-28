from libmgmt.base import Account
from libmgmt.actors import Member
from libmgmt.base import Person, Address

if __name__ == '__main__':
    acc = Account(1, "abc", Person("Karan", Address(), "ktandon1991@gmail.com", 12345))
    member = Member(1, "abc", Person("Karan", Address(), "ktandon1991@gmail.com", 123456))
    librarian = Member(2, "abc", Person("Sanjana", Address(), "ktandon1991@gmail.com", 123456))
    #Test logout without login
    member.logout()
    #check special admin without login
    librarian.reserve_book()
    ##log in
    member.login("abc")
    ## Reserving a book
    member.reserve_book()