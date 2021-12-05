class Agency:
    def __init__(self, name):
        self.name = name
        self.listings = []

    # implement + add needed parameters
    def add_listing_for_rent(self):
        pass

    # implement + add needed parameters
    def add_listing_for_sale(self):
        pass

    # implement
    def get_listings(self, for_sale=True, for_rent=True):
        pass

    # implement - should return most expensive listing for sale + for rent
    def get_most_expensive_listing(self):
        pass


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
