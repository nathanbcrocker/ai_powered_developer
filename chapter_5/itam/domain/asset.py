# Define a class named Asset
# It should have the following attributes: 
# - id: int
# - name: str
# - status: str
# - category: str
# - cost: float
# - useful_life: float
# - salvage_value: float
# - funding_details: FundingDetails
# 
# The attributes cannot be None and cannot be added after construction
# However, we should be able to access the attributes using methods

from dataclasses import dataclass
from datetime import date
from typing import List
from itam.domain.location import Location

@dataclass
class Asset():
    id: int
    name: str
    status: str
    category: str
    cost: float
    useful_life: int
    salvage_value: float
    purchase_date: date
    locations: List[Location]

    def __post_init__(self):
        if self.id is None:
            raise TypeError("ID cannot be None")
        if self.name is None:
            raise TypeError("Name cannot be None")
        if self.status is None:
            raise TypeError("Status cannot be None")
        if self.category is None:
            raise TypeError("Category cannot be None")
        if self.cost is None:
            raise TypeError("Cost cannot be None")
        if self.useful_life is None:
            raise TypeError("Useful life cannot be None")
        if self.salvage_value is None:
            raise TypeError("Salvage value cannot be None")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_status(self):
        return self.status

    def get_category(self):
        return self.category

    def get_cost(self):
        return self.cost

    def get_useful_life(self):
        return self.useful_life

    def get_salvage_value(self):
        return self.salvage_value

    def set_funding_details(self, funding_details):
        if (self.funding_details is None):
            self.funding_details = funding_details

    def get_funding_details(self):
        return self.funding_details
    
    def add_location(self, latitude: float, longitude: float, timestamp: date):
        location = Location(self.id, latitude, longitude, timestamp)
        self.locations.append(location)