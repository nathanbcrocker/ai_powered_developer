import unittest
from itam.visitor.department_visitor import DepartmentStatisticsVisitor
from itam.domain.asset import Asset
from itam.domain.department import Department
from itam.domain.funding_details import FundingDetails
from itam.domain.depreciation_strategy import DepreciationStrategy, StraightLineDepreciationStrategy, DoubleDecliningDepreciationStrategy
from datetime import date
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Location:
    name: str
    address: str

class TestDepartmentStatisticsVisitor(unittest.TestCase):
    def test_visit(self):
        visitor = DepartmentStatisticsVisitor()
        dept_it = Department(1, 'IT')
        dept_hr = Department(2, 'HR')

        asset1 = Asset(1, 'Computer', 'In use', 'Hardware', 1000.0, 3, 100.0, date.today(), [])
        asset2 = Asset(2, 'Printer', 'In use', 'Hardware', 500.0, 2, 50.0, date.today(), [])
        funding_details1 = FundingDetails(asset1, StraightLineDepreciationStrategy(), 0.33, { dept_it: 0.5, dept_hr: 0.5 })
        funding_details2 = FundingDetails(asset2, DoubleDecliningDepreciationStrategy(), 0.25, { dept_it: 0.3, dept_hr: 0.7 })
        asset1.set_funding_details(funding_details1)
        asset2.set_funding_details(funding_details2)

        visitor.visit(asset1)
        visitor.visit(asset2)
        self.assertEqual(visitor.get_total_cost(), 1500.0)
        self.assertEqual(visitor.get_total_depreciation(), 550.0)
        self.assertEqual(visitor.get_total_allocation(), 0.8)