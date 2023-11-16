# Define a class called InMemoryAssetRepository that inherits from the BaseRepository abstract class. 
# The InMemoryAssetRepository should be specific to managing Asset objects sing an in-memory list to store and update the assets. 
# Implement the necessary methods for CRUD operations such as create, read, update, and delete for Asset objects using the in-memory list. 
# Make sure to use type hints for the input parameters and return values.

from itam.infrastructure.repository.base_repository import BaseRepository
from itam.domain.asset import Asset

class InMemoryAssetRepository(BaseRepository[Asset]):
    def __init__(self):
        self._assets = []
    
    def create(self, asset: Asset) -> None:
        self._assets.append(asset)
    
    def read(self, asset_id: int) -> Asset:
        return next((asset for asset in self._assets if asset.id == asset_id), None)
    
    def update(self, asset: Asset) -> None:
        for i in range(len(self._assets)):
            if self._assets[i].id == asset.id:
                self._assets[i] = asset
                break
    
    def delete(self, asset_id: int) -> None:
        self._assets = [asset for asset in self._assets if asset.id != asset_id]
    
    def get_entities(self) -> list[Asset]:
        return self._assets