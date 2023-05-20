# create a class called Software, which is an instance of Asset. The Software entity has the following attributes:
# - id: int, 
# - name: str
# - version: str
# - license_key: str
# - vendor: str
# - status: str
# - department_percentages: Dict[Department, float]
# none of the attributes can be None
# define two methods specific to the Software entity: get_department_cost() and calculate_depreciation(). The get_department_cost() method calculates the cost of the asset for a given department, based on the percentages assigned to each department in the get_department_cost attribute. The calculate_depreciation() method calculates the depreciation of the asset using a given depreciation strategy.
# automatically generates special methods for a class that are commonly used for data objects

from typing import Dict
from dataclasses import dataclass
from itam.domain.department import Department
from itam.domain.depreciation_strategy import DepreciationStrategy
from itam.domain.asset import Asset

@dataclass
class Software(Asset):
    name: str
    version: str
    license_key: str
    vendor: str
    status: str
    department_percentages: Dict[Department, float]

    def __post_init__(self):
        if self.name is None:
            raise TypeError("Name cannot be None")
        if self.version is None:
            raise TypeError("Version cannot be None")
        if self.license_key is None:
            raise TypeError("License Key cannot be None")
        if self.vendor is None:
            raise TypeError("Vendor cannot be None")
        if self.status is None:
            raise TypeError("Status cannot be None")
        if self.department_percentages is None:
            raise TypeError("Line of Department Percentages cannot be None")

    def get_department_cost(self, department: Department) -> float:
        return self.cost * self.department_percentages[department]
    
    def calculate_depreciation(self, depreciation_strategy: DepreciationStrategy) -> float:
        return depreciation_strategy.calculate_depreciation(self.cost, self.purchase_date)