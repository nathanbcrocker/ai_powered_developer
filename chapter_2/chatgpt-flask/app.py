from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from asset import Asset
from asset_manager import AssetManager
from fastapi.responses import JSONResponse

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
    assets = asset_manager.get_all_assets()
    return JSONResponse(content=[asset.to_dict() for asset in assets])


@app.post("/assets/")
async def add_asset(asset: AssetIn):
    new_asset = Asset(asset.asset_id, asset.asset_type, asset.manufacturer, asset.model, asset.purchase_date, asset.warranty_end_date, asset.location)
    asset_manager.add_asset(new_asset)
    return {"message": "Asset added successfully"}

@app.delete("/assets/{asset_id}")
async def remove_asset(asset_id: str):
    if asset_manager.remove_asset(asset_id):
        return {"message": "Asset removed successfully"}
    else:
        return {"message": "Asset not found"}

@app.get("/assets/{asset_id}", response_model=AssetOut)
async def get_asset(asset_id: str):
    asset = asset_manager.get_asset_by_id(asset_id)
    if asset:
        return JSONResponse(content=asset.to_dict())
    else:
        return {"message": "Asset not found"}

@app.put("/assets/{asset_id}/assign")
async def assign_asset(asset_id: str, user: str):
    if asset_manager.assign_asset(asset_id, user):
        return {"message": "Asset assigned successfully"}
    else:
        return {"message": "Asset not available"}

@app.put("/assets/{asset_id}/unassign")
async def unassign_asset(asset_id: str):
    if asset_manager.unassign_asset(asset_id):
        return {"message": "Asset unassigned successfully"}
    else:
        return {"message": "Asset not assigned"}

@app.get("/assets/available/", response_model=List[AssetOut])
async def get_available_assets():
    assets = asset_manager.get_available_assets()
    return JSONResponse(content=[asset.to_dict() for asset in assets])

@app.get("/assets/assigned/", response_model=List[AssetOut])
async def get_assigned_assets():
    assets = asset_manager.get_assigned_assets()
    return JSONResponse(content=[asset.to_dict() for asset in assets])
