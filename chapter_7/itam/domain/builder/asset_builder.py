# Create a class called AssetBuilder
# It should use the Builder pattern to build an Asset
# Create another class called FundingDetailsBuilder
# It should use the Builder pattern to build a FundingDetails
# The AssetBuilder should have an embedded FundingDetailsBuilder
# When the category is "hardware" the AssetBuilder should create a Hardware object
# When the category is "software" the AssetBuilder should create a Software object
# When depreciation_strategy is equal to "straight_line" it should return a new instance of StraightLineDepreciationStrategy
# When depreciation_strategy is equal to "double_declining_balance" it should return a new instance of DoubleDecliningDepreciationStrategy
# When depreciation_strategy is equal to "none" it should return a new instance of NoDepreciationStrategy
# When depreciation_strategy is equal to "declining_balance" it should return a new instance of DecliningBalanceDepreciationStrategy
# The variables will need to be held in local variables and then passed to the Asset and FundingDetails objects when they are created.
# The final method of the AssetBuilder should return an Asset and be called build().
# The final method of the FundingDetailsBuilder should return a FundingDetails and be called build().

from datetime import datetime
from itam.domain.asset import Asset
from itam.domain.hardware import Hardware
from itam.domain.software import Software
from itam.domain.funding_details import FundingDetails
from itam.domain.depreciation_strategy import (
    DepreciationStrategy,
    StraightLineDepreciationStrategy,
    DecliningBalanceDepreciationStrategy,
    DoubleDecliningDepreciationStrategy,
    NoDepreciationStrategy
)

class AssetBuilder:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.category = ""
        self.cost = 0.0
        self.useful_life = 0
        self.status = ""
        self.salvage_value = 0.0
        self.purchase_date = datetime.now()

    def with_id(self, id: int):
        self.id = id
        return self

    def with_name(self, name: str):
        self.name = name
        return self

    def with_category(self, category: str):
        self.category = category
        return self

    def with_cost(self, cost: float):
        self.cost = cost
        return self

    def with_useful_life(self, useful_life: int):
        self.useful_life = useful_life
        return self

    def with_status(self, status: str):
        self.status = status
        return self

    def with_salvage_value(self, salvage_value: float):
        self.salvage_value = salvage_value
        return self

    def with_purchase_date(self, purchase_date: datetime):
        self.purchase_date = purchase_date
        return self

    def build(self) -> Asset:
        if self.category == "hardware":
            return Hardware(
                id=self.id,
                name=self.name,
                category=self.category,
                cost=self.cost,
                useful_life=self.useful_life,
                status=self.status,
                salvage_value=self.salvage_value,
                purchase_date=self.purchase_date
            )
        elif self.category == "software":
            return Software(
                id=self.id,
                name=self.name,
                category=self.category,
                cost=self.cost,
                useful_life=self.useful_life,
                status=self.status,
                salvage_value=self.salvage_value,
                purchase_date=self.purchase_date
            )
        else:
            return Asset(
                id=self.id,
                name=self.name,
                category=self.category,
                cost=self.cost,
                useful_life=self.useful_life,
                status=self.status,
                salvage_value=self.salvage_value,
                purchase_date=self.purchase_date
            )

class FundingDetailsBuilder:
    def __init__(self):
        self.asset = None
        self.depreciation_strategy = ""
        self.depreciation_rate = 0.0
        self.department_allocations = dict()

    def with_asset(self, asset: Asset):
        self.asset = asset
        return self

    def with_depreciation_strategy(self, depreciation_strategy: str):
        self.depreciation_strategy = depreciation_strategy
        return self

    def with_depreciation_rate(self, depreciation_rate: float):
        self.depreciation_rate = depreciation_rate
        return self
    
    def with_department_allocations(self, department_allocations: dict):
        self.department_allocations = department_allocations
        return self
    
    def build(self) -> FundingDetails:
        return FundingDetails(
            asset=self.asset,
            depreciation_strategy=self._get_depreciation_strategy(self.depreciation_strategy),
            depreciation_rate=self.depreciation_rate,
            department_allocations=self.department_allocations
        )

    def _get_depreciation_strategy(self, depreciation_strategy: str) -> DepreciationStrategy:
        if depreciation_strategy == "straight_line":
            return StraightLineDepreciationStrategy()
        elif depreciation_strategy == "double_declining_balance":
            return DoubleDecliningDepreciationStrategy()
        elif depreciation_strategy == "none":
            return NoDepreciationStrategy()
        elif depreciation_strategy == "declining_balance":
            return DecliningBalanceDepreciationStrategy()
        else:
            raise ValueError