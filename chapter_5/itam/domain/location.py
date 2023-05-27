# define the Location entity using Python's built-in dataclass decorator. 
# The Location entity has four attributes: id: int, name: str, address: Address, and organization: Organization which is optional.

from dataclasses import dataclass
from itam.domain.address import Address
from itam.domain.organization import Organization
from typing import Optional
from datetime import date

@dataclass
class Location:
    asset_id: int
    latitude: float
    longitude: float
    timestamp: date