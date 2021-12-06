from property import Property


class Listing:
    def __init__(self, property: Property, availability_date: str):
        self.property = property
        self.availability_date = availability_date

    def __str__(self):
        return f"{self.property}\nAvailable from: {self.availability_date}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.property.address}"


class RentListing(Listing):
    def __init__(self, property: Property, availability_date: str, monthly_rent: float, pets_allowed: bool):
        super().__init__(property, availability_date)
        self.monthly_rent = monthly_rent
        self.pets_allowed = pets_allowed


class SaleListing(Listing):
    def __init__(self, property: Property, availability_date: str, price: float):
        super().__init__(property, availability_date)
        self.price = price
