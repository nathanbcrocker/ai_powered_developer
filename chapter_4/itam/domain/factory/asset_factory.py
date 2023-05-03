# Define a class called AssetFactory
# It should have the following methods:
#        +new(self, asset_type: str, asset_name: str, asset_cost: float, useful_life: int, depreciation_strategy: str, depreciation_rate: float, salvage_value: float, asset_purchase_date: str) -> Asset
# Create a function that will take a string and return a datetime
# Use the AssetBuilder to create the Asset and use the FundingDetailsBuilder to create the FundingDetails

from datetime import datetime
from itam.domain.asset import Asset
from itam.domain.hardware import Hardware
from itam.domain.software import Software
from itam.domain.funding_details import FundingDetails
from itam.domain.builder.asset_builder import AssetBuilder, FundingDetailsBuilder

class AssetFactory:
    def __init__(self):
        self.id = 0

    def date_from_string(self, date_string: str) -> datetime:
        return datetime.strptime(date_string, "%Y-%m-%d")

    def new(self, asset_type: str, asset_name: str, asset_cost: float, useful_life: int, depreciation_strategy: str, depreciation_rate: float, salvage_value: float, asset_purchase_date: str) -> Asset:
        self.id += 1
        purchase_date = self.date_from_string(asset_purchase_date)
        a = AssetBuilder().with_id(self.id).with_name(asset_name).with_category(asset_type).with_cost(asset_cost).with_useful_life(useful_life).with_status("active").with_salvage_value(salvage_value).with_purchase_date(purchase_date).build()
        f = FundingDetailsBuilder().with_asset(a).with_depreciation_strategy(depreciation_strategy).with_depreciation_rate(depreciation_rate).build()

        a.funding_details = f
        return a