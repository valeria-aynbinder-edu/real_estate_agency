class RealEstateError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ParamsError(RealEstateError):
    pass
