"""
Test data module for car registration applications.

This module provides predefined test data objects for car registration testing,
including valid car registration examples with license plates and years.
"""

from functions.car_register_application import CarRegistrationApplication


def valid_car_registration():
    """Return a valid car registration object for testing purposes.
    
    Creates a CarRegistrationApplication instance with:
    - License plate: "KIK4567"
    - Year: 2017
    
    Returns:
        CarRegistrationApplication: A valid car registration object for testing
    """
    return CarRegistrationApplication(car_registration="KIK4567", year=2017)