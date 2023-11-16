# Define a class called AssetManager
# with CRUD operations for Asset
# and a method to notify observers whenever an asset is created, updated or deleted
# The AssetManager should accpet an instance of the BaseRepository[Asset] for data access and CRUD operations on Asset objects. 
# Implement methods for creating, reading, updating, and deleting assets using the AssetRepository instance. 
# Please include type hints for the input parameters and return values.
# The methods should be named create, read, update, get_assets, and delete.

from itam.domain.asset import Asset
from itam.infrastructure.mediators.asset_location_mediator import AssetLocationMediator
from itam.domain.events.asset_location_updated import AssetLocationUpdated
from itam.infrastructure.repository.base_repository import BaseRepository

class AssetManager:
    def __init__(self, base_repository: BaseRepository[Asset], mediator: AssetLocationMediator):
        self._repository = base_repository
        self.mediator = mediator
        self.mediator.register_handler(AssetLocationUpdated, self.update_asset_location)
    
    def create(self, asset: Asset) -> Asset:
        self._repository.create(asset)
        return asset
    
    def read(self, asset_id: int) -> Asset:
        return self._repository.read(asset_id)
    
    def update(self, asset: Asset) -> Asset:
        self._repository.update(asset)
        return asset
    
    def get_assets(self) -> list[Asset]:
        return self._repository.get_entities()
    
    def delete(self, asset_id: int) -> None:
        self._repository.delete(asset_id)

    def update_asset_location(self, event: AssetLocationUpdated) -> None:
        asset = self.read(event.asset_id)
        asset.add_location(event.latitude, event.longitude, event.timestamp)
        #self.update(asset)
        print(f"Asset {asset.id} location updated to {event.latitude}, {event.longitude} at {event.timestamp}")