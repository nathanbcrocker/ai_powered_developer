# import all of the classes from the domain module

from .asset import Asset
from .budget import Budget
from .depreciation_strategy import DepreciationStrategy, StraightLineDepreciationStrategy, DecliningBalanceDepreciationStrategy, DoubleDecliningDepreciationStrategy, NoDepreciationStrategy
from .funding_details import FundingDetails
from .hardware import Hardware
from .location import Location, Address
from .organization import Organization
from .software import Software
from .user import User
from .role import Role

__all__ = [
    "Asset",
    "Budget",
    "Software",
    "Hardware",
    "Department",
    "Organization",
    "Location",
    "Address",
    "DepreciationStrategy",
    "DecliningBalanceDepreciationStrategy",
    "StraightLineDepreciationStrategy",
    "DoubleDecliningDepreciationStrategy",
    "NoDepreciationStrategy",
    "Organization",
    "User",
    "Role",
    "FundingDetails"
]
