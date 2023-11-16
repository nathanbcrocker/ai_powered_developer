# Define a class called FundingDetails
# It should have the following attributes: 
# - depreciation_strategy: DepreciationStrategy,
# - depreciation_rate: float
# - department_allocations: Dict[Department, float]
# The attributes cannot be None and cannot be modified after construction
# However, we should be able to access the attributes using methods

from dataclasses import dataclass
from itam.domain.depreciation_strategy import DepreciationStrategy
from itam.domain.department import Department
from typing import Dict


@dataclass
class FundingDetails:
    depreciation_rate: float
    department_allocations: Dict[Department, float]
    depreciation_strategy: DepreciationStrategy or 'itam.domain.depreciation_strategy.DepreciationStrategy'
    asset: None or 'itam.domain.asset.Asset'

    def get_depreciation_rate(self):
        return self.depreciation_rate

    def get_department_allocations(self):
        return self.department_allocations

    def get_depreciation_strategy(self):
        return self.depreciation_strategy

    def get_asset(self):
        return self.asset
