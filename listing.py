from property import Property


class Listing:
    def __init__(self, property: Property, availability_date: str):
        self.property = property
        self.availability_date = availability_date


class RentListing(Listing):
    def __init__(self, property: Property, availability_date: str, monthly_rent: float, pets_allowed: bool):
        super().__init__(property, availability_date)
        self.monthly_rent = monthly_rent
        self.pets_allowed = pets_allowed


class SaleListing(Listing):
    def __init__(self, property: Property, availability_date: str, price: float):
        super().__init__(property, availability_date)
        self.price = price
