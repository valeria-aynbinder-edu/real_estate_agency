from abc import ABC


class Customer(ABC):
    def __init__(self, id, full_name, address, email, phone):
        self.id = id
        self.full_name = full_name
        self.address = address
        self.email = email
        self.phone = phone


class Owner(Customer):
    def __init__(self, id, full_name, address, email, phone, listings):


class Seeker(Customer):
    pass