class Error(Exception):
    """Base-class for the exceptions"""


class InvalidDensityError(Error):
    """the density should not be negative"""



def determine_weight(weight, density):
    if density < 0:
        raise InvalidDensityError("density should not be negative")
    return 10