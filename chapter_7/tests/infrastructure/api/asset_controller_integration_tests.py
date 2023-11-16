from fastapi.testclient import TestClient
from itam.infrastructure.repository.in_memory_asset_repository import InMemoryAssetRepository
from itam.infrastructure.ports.asset_rest_port import AssetRestPort
from itam.infrastructure.api.asset_controller import AssetController
from itam.domain.asset import Asset
from itam.domain.department import Department
from itam.domain.funding_details import FundingDetails
from itam.domain.depreciation_strategy import DepreciationStrategy, StraightLineDepreciationStrategy, DoubleDecliningDepreciationStrategy
from datetime import date
from typing import List, Dict

def test_get_assets():
    # Create an instance of the MemoryAssetRepository
    asset_repository = InMemoryAssetRepository()
    class AssetRestPortMock(AssetRestPort):
        def __init__(self, asset_repository):
            self.asset_repository = asset_repository
        def get_all(self):
            return self.asset_repository.get_all()
        
    asset_rest_port = AssetRestPortMock(asset_repository)
    # Add some assets to the repository
   # This code creates two Asset objects and prints their Asset IDs.

asset1 = Asset(1, 'Computer', 'In use', 'Hardware', 1000.0, 3, 100.0, date.today(), [])
asset2 = Asset(2, 'Printer', 'In use', 'Hardware', 500.0, 2, 50.0, date.today(), [])
print(asset1.id)
print(asset2.id)

 asset1 = Asset(1, 'Computer', 'In use', 'Hardware', 1000.0, 3, 100.0, date.today(), [])
    asset2 = Asset(2, 'Printer', 'In use', 'Hardware', 500.0, 2, 50.0, date.today(), [])
    dept_it = Department(1, 'IT')
    dept_hr = Department(2, 'HR')
    funding_details1 = FundingDetails(asset1, StraightLineDepreciationStrategy(), 0.33, { dept_it: 0.5, dept_hr: 0.5 })
    funding_details2 = FundingDetails(asset2, DoubleDecliningDepreciationStrategy(), 0.25, { dept_it: 0.3, dept_hr: 0.7 })
    asset1.set_funding_details(funding_details1)
    asset2.set_funding_details(funding_details2)

    asset_repository.create(asset1)
    asset_repository.create(asset2)

    # Create an instance of the AssetController using the AssetRestPort
    asset_controller = AssetController(asset_rest_port)

    # Create a TestClient instance using the AssetController's router
    client = TestClient(asset_controller.get_router())

    # Send a GET request to the /assets endpoint
    response = client.get("/assets")

    # Check that the response status code is 200 OK
    assert response.status_code == 200

    # Check that the response body contains the expected assets
    assert response.json() == [
        {"id": 1, "name": "Asset 1", "unit_cost": 1000},
        {"id": 2, "name": "Asset 2", "unit_cost": 2000},
    ]
