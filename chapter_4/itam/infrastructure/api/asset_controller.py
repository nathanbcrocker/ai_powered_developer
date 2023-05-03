# Define a class called AssetController
# It should accept an object of type AssetRestPort as a constructor parameter. 
# In the constructor it should define a FastAPI router object and assign it to a private attribute
# The AssetController should use this object to interact with the Asset Manager through the AssetRestPort interface.
# Implementation of error handling, logging, and other necessary components for a robust and reliable HTTP API
# All methods should be asynchronous

from fastapi import APIRouter, HTTPException
from itam.domain.asset import Asset
from itam.domain.factory.asset_factory import AssetFactory
from itam.infrastructure.api.asset_model import AssetIn, AssetOut, from_asset
from itam.infrastructure.ports.asset_rest_port import AssetRestPort
import logging

class AssetController:
    def __init__(self, asset_rest_port:  AssetRestPort):
        self._asset_factory = AssetFactory()
        self._asset_rest_port = asset_rest_port
        self._router = APIRouter()
        self._router.get("/assets", response_model=list[AssetOut])(self.get_assets)
        self._router.get("/assets/{asset_id}", response_model=AssetOut)(self.get_asset)
        self._router.post("/assets", response_model=AssetOut)(self.create_asset)
        self._router.put("/assets/{asset_id}", response_model=AssetOut)(self.update_asset)
        self._router.delete("/assets/{asset_id}", response_model=AssetOut)(self.delete_asset)

    def get_router(self):
        return self._router

    async def get_assets(self):
        return  [ from_asset(a) for a in self._asset_rest_port.get_assets()]

    async def get_asset(self, asset_id: int):
        asset = self._asset_rest_port.read(asset_id)
        if asset is None:
            raise HTTPException(status_code=404, detail="Asset not found")
        return from_asset(asset)
    
    async def create_asset(self, asset_in: AssetIn):
        asset = self._asset_factory.new(asset_in.asset_type, asset_in.name, asset_in.unit_cost, asset_in.useful_life, asset_in.depreciation_strategy, asset_in.depreciation_rate, asset_in.salvage_value, asset_in.purchase_date)
        self._asset_rest_port.create(asset)
        return from_asset(asset)

    async def update_asset(self, asset_id: int, asset_in: AssetIn):
        asset = self._asset_factory.new(asset_in.asset_type, asset_in.name, asset_in.unit_cost, asset_in.useful_life, asset_in.depreciation_strategy, asset_in.depreciation_rate, asset_in.salvage_value, asset_in.purchase_date)
    
        asset.id = asset_id
        asset = self._asset_rest_port.update(asset)
        if asset is None:
            raise HTTPException(status_code=404, detail="Asset not found")
        return from_asset(asset)

    async def delete_asset(self, asset_id: int):
        asset = self._asset_rest_port.read(asset_id)
        if asset is None:
            raise HTTPException(status_code=404, detail="Asset not found")
        self._asset_rest_port.delete(asset_id)
        return from_asset(asset)
