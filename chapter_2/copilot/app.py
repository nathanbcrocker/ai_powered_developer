# Create a FastAPI app that allows CRUD operations on the Asset class.
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from asset import Asset
from asset_manager import AssetManager

app = FastAPI()
asset_manager = AssetManager()

class AssetIn(BaseModel):
    asset_id: str
    asset_type: str
    manufacturer: str
    model: str
    purchase_date: str
    warranty_end_date: str
    location: str

class AssetOut(BaseModel):
    asset_id: str
    asset_type: str
    manufacturer: str
    model: str
    purchase_date: str
    warranty_end_date: str
    location: str
    assigned_to: Optional[str] 
    status: str

@app.get("/assets/", response_model=List[AssetOut])
async def get_assets():
    assets = asset_manager.get_assets()
    return JSONResponse(content=[asset.to_dict() for asset in assets])


@app.post("/assets/")
async def add_asset(asset: AssetIn):
    new_asset = Asset(asset.asset_id, asset.asset_type, asset.manufacturer, asset.model, asset.purchase_date, asset.warranty_end_date, asset.location)
    asset_manager.add_asset(new_asset)
    return {"message": "Asset added successfully"}