from agency import Agency
from errors import ParamsError
from listing import Listing, RentListing, SaleListing
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

    # Creation of listings
    # 1.The first property is both for rent for $2K per month and
    # for sale for $800K. Available starting from 01-01-2022
    flat_for_rent_listing = RentListing(flat, '01-01-2022', 2000, pets_allowed=False)
    flat_for_sale_listing = SaleListing(flat, '01-01-2022', 800000)

    # 2.This property is for sale for $2M, available from 01-04-2023
    villa_for_sale = SaleListing(villa, '01-04-2023', 2000000)

    # 3. For rent for $20K per month
    commercial_for_rent = RentListing(commercial, '01-04-2023', 20000, pets_allowed=False)

    agency = Agency("ZebraRealEstate")
    agency.add_listing(flat_for_rent_listing)
    agency.add_listing(flat_for_sale_listing)
    agency.add_listing(villa_for_sale)
    agency.add_listing(commercial_for_rent)

    try:
        print(agency.get_listings(for_sale=False, for_rent=False))
    except ParamsError as error:
        print(f"There is a problem: {error}")
    print(agency.get_most_expensive_listing())





