class Property:
    def __init__(self, country, city, address, parking_places, sq_m):
        self.country = country
        self.city = city
        self.address = address
        self.parking_places = parking_places
        self.sq_m = sq_m

    def __str__(self):
        return f"{self.str_repr_title()}\n{self.str_repr_address()}\n{self.str_repr_optional()}"

    def str_repr_title(self):
        return "Property"

    def str_repr_address(self):
        return f"{self.country}, {self.city}\n{self.address}"

    def str_repr_optional(self):
        return ""


class Residential(Property):
    def __init__(self, country, city, address, parking_places, sq_m, rooms_num, has_balcony):
        super().__init__(country, city, address, parking_places, sq_m)
        self.rooms_num = rooms_num
        self.has_balcony = has_balcony

    def str_repr_title(self):
        return "Residential Property"

    def str_repr_optional(self):
        return f"Rooms: {self.rooms_num}\nHas balcony: {self.has_balcony}"


class Commercial(Property):
    def __init__(self, country, city, address, parking_places, sq_m, allowed_activities=set()):
        super().__init__(country, city, address, parking_places, sq_m)
        self.allowed_activities = allowed_activities

    def add_activity(self, *args):
        self.allowed_activities.update(args)


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
