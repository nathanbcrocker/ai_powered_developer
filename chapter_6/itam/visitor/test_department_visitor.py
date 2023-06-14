import unittest
from itam.visitor import DepartmentStatisticsVisitor
from itam.domain.asset import Asset
from itam.domain.department import Department
from itam.domain.funding_details import FundingDetails
from itam.domain.depreciation_strategy import StraightLineDepreciationStrategy, DoubleDecliningDepreciationStrategy
from datetime import date
from typing import List, Dict

class TestDepartmentStatisticsVisitor(unittest.TestCase):
    def test_visit(self):
        visitor = DepartmentStatisticsVisitor()
        dept_it = Department(1, 'IT')
        dept_hr = Department(2, 'HR')


        funding_details1 = FundingDetails(0.33, { dept_it: 0.5, dept_hr: 0.5 }, StraightLineDepreciationStrategy(), None)
        funding_details2 = FundingDetails(0.25, { dept_it: 0.3, dept_hr: 0.7 }, DoubleDecliningDepreciationStrategy(), None)

        asset1 = Asset(id=1, name='Computer', status='In use', category='Hardware', cost=1000.0, useful_life=3, salvage_value=100.0, purchase_date=date.today(), locations=[], funding_details=funding_details1)
        asset2 = Asset(id=2, name='Printer', status='In use', category='Hardware', cost=500.0, useful_life=2,salvage_value=50.0, purchase_date=date.today(), locations=[], funding_details=funding_details2)


        #asset1.set_funding_details(funding_details1)
        #asset2.set_funding_details(funding_details2)

        visitor.visit(asset1)
        visitor.visit(asset2)
        self.assertEqual(visitor.get_total_cost(), 1500.0)
        self.assertEqual(visitor.get_total_depreciation(), 1300.0)
        #self.assertEqual(visitor.get_total_allocation(), 0.8)