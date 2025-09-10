"""
Test data module for car registration applications.

This module provides predefined test data objects for car registration testing,
including valid car registration examples with license plates and years.
"""

from functions.car_register_application import CarRegistrationApplication


def valid_car_registration_2015():
    """Return a valid car registration object for testing purposes.
    
    Creates a CarRegistrationApplication instance with:
    - License plate: "RTU2945"
    - Year: 2015
    
    Returns:
        CarRegistrationApplication: A valid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="RTU9999", year=2015)

def valid_car_registration_2016():
    """Return a valid car registration object for testing purposes.
    
    Creates a CarRegistrationApplication instance with:
    - License plate: "MNO2945"
    - Year: 2016
    
    Returns:
        CarRegistrationApplication: A valid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="MNO2945", year=2016)

def valid_car_registration_2017():
    """Return a valid car registration object for testing purposes.
    
    Creates a CarRegistrationApplication instance with:
    - License plate: "NIK0000"
    - Year: 2017
    
    Returns:
        CarRegistrationApplication: A valid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="NIK0000", year=2017)


# Invalid car registration test data objects

def invalid_car_registration_too_few_letters():
    """Return an invalid car registration object with too few letters (2 letters + 4 numbers).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="KI4567", year=2015)


def invalid_car_registration_too_many_letters():
    """Return an invalid car registration object with too many letters (4+ letters + 4 numbers).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="JULI1234", year=2017)


def invalid_car_registration_too_few_numbers():
    """Return an invalid car registration object with too few numbers (3 letters + 3 numbers).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="ABC123", year=2016)


def invalid_car_registration_too_many_numbers():
    """Return an invalid car registration object with too many numbers (3 letters + 5+ numbers).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="XYZ12345", year=2015)


def invalid_car_registration_lowercase_letters():
    """Return an invalid car registration object with lowercase letters (3 lowercase + 4 numbers).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="def7890", year=2017)


def invalid_car_registration_mixed_case_letters():
    """Return an invalid car registration object with mixed case letters (mixed case + 4 numbers).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="GhI5678", year=2017)


def invalid_car_registration_special_characters():
    """Return an invalid car registration object with special characters (3 letters + special chars + numbers).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="MNO-9012", year=2017)


def invalid_car_registration_empty():
    """Return an invalid car registration object with empty license plate.
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="", year=2017)


def invalid_car_registration_numbers_first():
    """Return an invalid car registration object with numbers before letters (4 numbers + 3 letters).
    
    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="3456PQR", year=2017)


def invalid_car_registration_no_year_selected():
    """Return an invalid car registration object for testing purposes, without year selection.

    Creates a CarRegistrationApplication instance with:
    - License plate: "RTU2945"
    - Year: Select a year

    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="RTU2945", year="Select a year")


def invalid_car_registration_greek_letters():
    """Return an invalid car registration object for testing purposes with greek letters.

    Creates a CarRegistrationApplication instance with:
    - License plate: "ΜΝΟ2945"
    - Year: 2016
    WARNING: ΜΝΟ is written in greek letters.

    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="ΜΝΟ2945", year=2016)


def invalid_car_registration_romanian_pattern():
    """Return an invalid car registration object for testing purposes with romanian pattern.

    Creates a CarRegistrationApplication instance with:
    - License plate: "BN18CTL"
    - Year: 2016

    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="BN18CTL", year=2016)

def invalid_car_registration_with_space():
    """Return an invalid car registration object for testing purposes with space.

    Creates a CarRegistrationApplication instance with:
    - License plate: "RTU 2945"
    - Year: 2016

    Returns:
        CarRegistrationApplication: An invalid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="RTU 2945", year=2016)