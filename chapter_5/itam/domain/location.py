# define the Location entity using Python's built-in dataclass decorator. 
# The Location entity has four attributes: id: int, name: str, address: Address, and organization: Organization which is optional.

from dataclasses import dataclass
from itam.domain.address import Address
from itam.domain.organization import Organization
from typing import Optional

@dataclass
class Location:
    id: int
    name: str
    address: Address
    organization: Optional[Organization]

    def __post_init__(self):
        if self.id is None:
            raise TypeError("Id cannot be None")
        if self.name is None:
            raise TypeError("Name cannot be None")
        if self.address is None:
            raise TypeError("Address cannot be None")
        if self.organization is None:
            raise TypeError("Organization cannot be None")