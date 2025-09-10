from functions.car_register_application import CarRegistrationApplication


def valid_car_registration():
    """Return a valid car registration object"""
    return CarRegistrationApplication(car_registration="KIK4567", year=2017)