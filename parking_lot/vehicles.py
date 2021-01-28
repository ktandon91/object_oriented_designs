from parking_lot.base import Vehicle
from parking_lot.types_and_status import VehicleType

class LMV(Vehicle):
    def __init__(self, licensenumber, type=VehicleType.LMV):
        super().__init__(licensenumber, type)

    def assign_ticket(self):
        pass

class TwoWheeler(Vehicle):
    def __init__(self, licensenumber, type=VehicleType.TWOWHEELER):
        super().__init__(licensenumber, type)

    def assign_ticket(self):
        pass

class HMV(Vehicle):
    def __init__(self, licensenumber, type=VehicleType.HMV):
        super().__init__(licensenumber, type)

    def assign_ticket(self):
        pass