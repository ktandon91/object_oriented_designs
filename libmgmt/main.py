from libmgmt.actors import Member
from libmgmt.base import Person, Address

if __name__ == '__main__':
    member = Member(1, "abc", Person("Karan", Address(), "ktandon1991@gmail.com", 123456))
    ##log in
    member.login("abc")
    ## Reserving a book
    member.reserve_book()