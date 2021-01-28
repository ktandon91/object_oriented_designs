from enum import Enum

class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE = 1, 2, 3, 4

class VehicleType(Enum):
    TWOWHEELER, LMV, HMV = 1, 2, 3

class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST, = 1, 2, 3

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED = 1, 2, 3, 4

class UserLoginStatus(Enum):
    ANONYMOUS, LOGGED_IN = 1, 2
