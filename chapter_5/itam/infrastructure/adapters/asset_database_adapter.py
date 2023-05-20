# Create a class called AssetDatabaseAdapter that implements the DatabasePort interface
# This class will handle the database operations using a SQLAlchemy session. 
# The adapter should interact with Asset. 
# Implement methods for creating, getting, updating, and deleting assets, as well as listing all assets. 
# The adapter should not interact with the domain model directly.
# The get_asset method should return a single Asset based off of the asset_id parameter.
# The get_assets method should return a list of all assets from the database.
# The create method should take an Asset object as a parameter and create a new row in the database as well as return the new Asset object.
# The update method should take an asset_id and an Asset object as parameters and update the row in the database that matches the asset_id.
# The delete method should take an asset_id as a parameter and delete the row in the database that matches the asset_id.
# Create, update, and detele methods should return the updated Asset object.

from itam.domain.asset import Asset
from itam.infrastructure.ports.asset_database_port import AssetDatabasePort
from sqlalchemy.orm import Session

class AssetDatabaseAdapter(AssetDatabasePort):
    def __init__(self, session: Session):
        self._session = session
    
    def get_asset(self, asset_id: int) -> Asset:
        return self._session.query(Asset).filter(Asset.id == asset_id).first()
    
    def get_assets(self) -> list:
        return self._session.query(Asset).all()
    
    def create(self, asset: Asset) -> Asset:
        self._session.add(asset)
        self._session.commit()
        return asset
    
    def update(self, asset_id: int, asset: Asset) -> Asset:
        self._session.query(Asset).filter(Asset.id == asset_id).update(asset)
        self._session.commit()
        return asset
    
    def delete(self, asset_id: int) -> None:
        self._session.query(Asset).filter(Asset.id == asset_id).delete()
        self._session.commit()






