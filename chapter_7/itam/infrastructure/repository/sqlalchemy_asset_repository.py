# Define a class called SQLAlchemyAssetRepository that implements the AssetRepository interface for data access using SQLAlchemy. 
# The class should handle the CRUD operations (create, read, update, and delete) for assets, storing and retrieving them in a PostgreSQL database using SQLAlchemy.

from itam.domain.asset import Asset
from itam.domain.location import Location
from itam.domain.funding_details import FundingDetails
from itam.domain.depreciation_strategy import DepreciationStrategy, StraightLineDepreciationStrategy, DoubleDecliningDepreciationStrategy
from itam.infrastructure.repository.base_repository import BaseRepository
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import Session, relationship
from typing import List
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class FundingDetailsModel(Base):
    __tablename__ = 'funding_details'
    id = Column(Integer, primary_key=True)
    depreciation_rate = Column(Float)
    depreciation_strategy_id = Column(Integer)

    def get_depreciation_strategy(self) -> DepreciationStrategy:
        if self.depreciation_strategy_id is 1:
            return StraightLineDepreciationStrategy()
        else:
            return DoubleDecliningDepreciationStrategy()

class AssetModel(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    status = Column(String)
    category = Column(String)
    cost = Column(Float)
    useful_life = Column(Float)
    salvage_value = Column(Float)
    purchase_date = Column(Date)
    funding_details_id = Column(Integer, ForeignKey('funding_details.id'))
    funding_details = relationship('FundingDetailsModel')

class LocationModel(Base):
    __tablename__ = 'asset_locations'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(Date)
    asset_id = Column(Integer, ForeignKey('assets.id'))
    asset = relationship('AssetModel')

    def to_domain(self, asset_id: int) -> Location:
        return Location(asset_id=asset_id, latitude=self.latitude, longitude=self.longitude, timestamp=self.timestamp)


class SQLAlchemyAssetRepository(BaseRepository[Asset]):
    def __init__(self, session: Session):
        self._session = session
    
    def create(self, asset: Asset) -> Asset:
        self._session.add(asset)
        self._session.commit()
        return asset

    def read(self, asset_id: int) -> Asset:
        asset = self._session.query(AssetModel).filter(AssetModel.id == asset_id).first()
        fd = FundingDetails(depreciation_strategy=asset.funding_details.get_depreciation_strategy(),
                            depreciation_rate=asset.funding_details.depreciation_rate,
                            department_allocations={}, asset=None)

        a = Asset(id=asset.id, name=asset.name, status=asset.status, category=asset.category, cost=asset.cost, useful_life=asset.useful_life, salvage_value=asset.salvage_value, purchase_date=asset.purchase_date, locations=[], funding_details=fd)
        fd.asset = a
        return a
    
    def update(self, asset: Asset) -> Asset:
        self._session.query(AssetModel).filter(AssetModel.id == asset.id).update({AssetModel.name: asset.name, AssetModel.status: asset.status, AssetModel.category: asset.category, AssetModel.cost: asset.cost, AssetModel.useful_life: asset.useful_life, AssetModel.salvage_value: asset.salvage_value, AssetModel.purchase_date: asset.purchase_date})
        self._session.commit()
        return asset
    
    def get_entities(self) -> List[Asset]:
        assets = self._session.query(AssetModel).all()
        a_list = []
        for asset in assets:
            if asset.funding_details == None: 
                print(asset.id)
                continue

            fd = FundingDetails(depreciation_strategy=asset.funding_details.get_depreciation_strategy(),
                                depreciation_rate=asset.funding_details.depreciation_rate, department_allocations={}, asset=None)

            a = Asset(id=asset.id, name=asset.name, status=asset.status, category=asset.category, cost=asset.cost, useful_life=asset.useful_life, salvage_value=asset.salvage_value, purchase_date=asset.purchase_date, locations=[], funding_details=fd)
            fd.asset = a
            a_list.append(a)

        return a_list
    
    def delete(self, asset_id: int) -> None:
        self._session.query(AssetModel).filter(AssetModel.id == asset_id).delete()
        self._session.commit()

    def get_funding_details(self, asset_id: int) -> List[FundingDetailsModel]:
        funding_details = self._session.query(FundingDetailsModel).filter(FundingDetailsModel.asset_id == asset_id).all()
        return funding_details

    def get_locations(self, asset_id: int) -> List[Location]:
        assest_locations = self._session.query(LocationModel).filter(LocationModel.asset_id == asset_id).all()
        locations = [asset_location.to_domain(asset_id) for asset_location in assest_locations]
        return locations