class Property:
    def __init__(self, country, city, address, parking_places, sq_m):
        self.country = country
        self.city = city
        self.address = address
        self.parking_places = parking_places
        self.sq_m = sq_m


class Residential(Property):
    def __init__(self, country, city, address, parking_places, sq_m, rooms_num, has_balcony):
        super().__init__(country, city, address, parking_places, sq_m)
        self.rooms_num = rooms_num
        self.has_balcony = has_balcony


class Commercial(Property):
    def __init__(self, country, city, address, parking_places, sq_m, allowed_activities=[]):
        super().__init__(country, city, address, parking_places, sq_m)
        self.allowed_activities = allowed_activities


class Flat(Residential):
    def __init__(self, country, city, address, parking_places, sq_m, rooms_num, has_balcony, floor, has_elevator):
        super().__init__(country, city, address, parking_places, sq_m, rooms_num, has_balcony)
        self.floor = floor
        self.has_elevator = has_elevator


class Villa(Residential):
    def __init__(self, country, city, address, parking_places, sq_m, rooms_num, has_balcony, floors_num, has_pool, garden_sq_m):
        super().__init__(country, city, address, parking_places, sq_m, rooms_num, has_balcony)
        self.floors_num = floors_num
        self.has_pool = has_pool
        self.garden_sq_m = garden_sq_m
