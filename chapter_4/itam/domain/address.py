# Define the Address entity using Python's built-in dataclass decorator. 
# The Address entity has four attributes: street: str, city: str, state: str, and zip_code: str.

from dataclasses import dataclass

@dataclass
class Address:
    street: str
    city: str
    state: str
    zip_code: str

    def __post_init__(self):
        if self.street is None:
            raise TypeError("Street cannot be None")
        if self.city is None:
            raise TypeError("City cannot be None")
        if self.state is None:
            raise TypeError("State cannot be None")
        if self.zip_code is None:
            raise TypeError("Zip Code cannot be None")