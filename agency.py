from listing import Listing, SaleListing, RentListing


class Agency:
    def __init__(self, name):
        self.name = name
        self.listings = []

    # implement + add needed parameters
    def add_listing(self, listing: Listing):
        self.listings.append(listing)

    # implement
    def get_listings(self, for_sale=True, for_rent=True):
        ret_list = []
        for listing in self.listings:
            if (for_sale and isinstance(listing, SaleListing)) or \
                    (for_rent and isinstance(listing, RentListing)):
                ret_list.append(listing)
        return ret_list

    # implement - should return most expensive listing for sale + for rent
    def get_most_expensive_listing(self):
        max_sale_listing = None
        max_rent_listing = None
        # todo: valeria discuss options to improve performance
        for l in self.listings:
            if isinstance(l, RentListing) and l.monthly_rent > max_rent_listing.monthly_rent:
                max_rent_listing = l
            if isinstance(l, SaleListing) and l.price > max_sale_listing.price:
                max_sale_listing = l
        return max_sale_listing, max_rent_listing


    # Bonus: implement a method that returns hierarchical structure of the listing as dictionary
    # according to *args received
    # For example: for args: listing_type, country, property_type, you should return
    # a dictionary in the following format:
    # {
    #   "for_sale": {
    #           "commertial": [listing1, listing2, ...],
    #           "flat": [listing1, listing2, ...],
    #           "villa": [listing1,...]
    #       },
    #   "for_rent": {
    #            ...
    #       }
    # }
    #
    # Available options are: listing_type, country, city, property_type
    def get_listings_hierarchical(self, *args):
        pass
