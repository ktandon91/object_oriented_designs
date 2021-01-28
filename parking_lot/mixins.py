class NormalCustomerOperationsMixin:
    def take_ticket(self):
        pass

    def scan_ticket(self):
        pass

class AdminOperationsMixin:
    def add_parking_spot(self):
        pass

    def add_parking_floor(self):
        pass

    def add_parking_attendant(self, parking_attendant):
        pass

class GeneralAccountOperationsMixin:
    def view_account(self):
        pass

    def update_account(self):
        pass

class SpecialParkingAttendantOperationsMixin:
    def cash_payment(self):
        pass

