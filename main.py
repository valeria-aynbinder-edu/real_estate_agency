from property import Flat, Villa, Commercial, Property

ISRAEL = 'Israel'

if __name__ =='__main__':
    # 3-rooms flat, 78 square meters, in the building with elevator,
    # located in Israel, Tel-Aviv, Dizengoff 32, no parking, with balcony
    flat = Flat(country=ISRAEL, city='Tel-Aviv', address='Dizengoff 32',
                     parking_places=0, sq_m=78, rooms_num=3,
                     has_balcony=True, floor=2, has_elevator=True)

    # Villa with 8 rooms, 200 sq_m in Herzliya, Hertzl 5, 3 floors, 3 balconies,
    # 4 parking places, with swimming pool, 300 sq_meter gardern
    villa = Villa(country=ISRAEL, city='Herzliya', address='Hertzl 5',
                  parking_places=4, sq_m=200, rooms_num=8,
                  has_balcony=True, floors_num=3, has_pool=True, garden_sq_m=300)

    # Commercial property that can be used as store or caffe,
    # the property located in London, Britain, Oxford street 47.
    # There is a parking lot suitable for 10 cars.
    # The area of the property is 500 square meters
    commercial = Commercial(country='Britain', city='London', address='Oxford 47',
                            parking_places=10, sq_m=500)
    commercial.add_activity('store', 'caffe')

    print(flat)

    print("test property print")
    prop = Property(country='France', city='Paris', address='blabla 47',
                            parking_places=1, sq_m=500)
    print(prop)
