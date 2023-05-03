# Define a class called SQLAlchemyAssetRepository that implements the AssetRepository interface for data access using SQLAlchemy. 
# The class should handle the CRUD operations (create, read, update, and delete) for assets, storing and retrieving them in a PostgreSQL database using SQLAlchemy.

from itam.domain.asset import Asset
from itam.infrastructure.repository.base_repository import BaseRepository
from sqlalchemy.orm import Session

class SQLAlchemyAssetRepository(BaseRepository[Asset]):
    def __init__(self, session: Session):
        self._session = session
    
    def create(self, asset: Asset) -> Asset:
        self._session.add(asset)
        self._session.commit()
        return asset
    
    def read(self, asset_id: int) -> Asset:
        return self._session.query(Asset).filter(Asset.id == asset_id).first()
    
    def update(self, asset: Asset) -> Asset:
        self._session.query(Asset).filter(Asset.id == asset.id).update(asset)
        self._session.commit()
        return asset
    
    def get_assets(self) -> list[Asset]:
        return self._session.query(Asset).all()
    
    def delete(self, asset_id: int) -> None:
        self._session.query(Asset).filter(Asset.id == asset_id).delete()
        self._session.commit()