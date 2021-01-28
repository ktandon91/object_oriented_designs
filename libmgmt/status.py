from enum import Enum

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELLED, BLACKLISTED = 1,2,3,4

class UserStatus(Enum):
    ANONYMOUS, LOGGED_IN = 1, 2

class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
    WAITING, PENDING, COMPLETED, CANCELED = 1, 2, 3, 4

class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIOBOOK, EBOOK = 1, 2, 3, 4