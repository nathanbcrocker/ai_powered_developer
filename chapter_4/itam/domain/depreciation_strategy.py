# Define an interface called DepreciationStrategy. 
# It should have four concrete implementations of the interface: StraightLineDepreciationStrategy, DecliningBalanceDepreciationStrategy, DoubleDecliningDepreciationStrategy, and NoDepreciationStrategy.
# Each implementation overrides the calculate_depreciation() method to provide a specific way of calculating depreciation for an asset based on its funding details.
# The calculate_depreciation() method should take a FundingDetails object as a parameter and return a float value representing the depreciation amount.
# NoDepreciationStrategy should return 0 for all assets.
# The other three strategies should return the depreciation amount based on the following formulas:
# - Straight Line: (cost - salvage value) / useful_life
# - Declining Balance: cost * (1-rate/100)^(current_year - purchase_year)
# - Double Declining: Declining Balance * 2

from abc import ABC, abstractmethod
from itam.domain.asset import Asset
from math import pow
from datetime import datetime

class DepreciationStrategy(ABC):
    @abstractmethod
    def calculate_depreciation(self, asset: Asset) -> float:
        pass

class StraightLineDepreciationStrategy(DepreciationStrategy):
    def calculate_depreciation(self, asset: Asset) -> float:
        cost = asset.get_cost()
        salvage_value = asset.get_salvage_value()
        useful_life = asset.get_useful_life()
        return (cost - salvage_value) / useful_life

class DecliningBalanceDepreciationStrategy(DepreciationStrategy):
    def calculate_depreciation(self, asset: Asset) -> float:
        cost = asset.get_cost()
        depreciation_rate = asset.get_depreciation_rate()
        return cost * pow(1 - (depreciation_rate / 100), datetime.now().year - asset.get_purchase_date().year)

class DoubleDecliningDepreciationStrategy(DepreciationStrategy):
    def calculate_depreciation(self, asset: Asset) -> float:
        return DecliningBalanceDepreciationStrategy().calculate_depreciation(asset) * 2
    
class NoDepreciationStrategy(DepreciationStrategy):
    def calculate_depreciation(self, asset: Asset) -> float:
        return 0