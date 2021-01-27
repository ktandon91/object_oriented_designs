from enum import Enum

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELLED, BLACKLISTED = 1,2,3,4

class UserStatus(Enum):
    ANONYMOUS, LOGGED_IN = 1, 2