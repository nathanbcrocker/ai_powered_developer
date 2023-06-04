from datetime import date

class AssetLocationUpdated:
    def __init__(self, asset_id: int, latitude: float, longitude: float, timestamp: date):
        self.asset_id = asset_id
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = timestamp