from typing import List, Optional
from asset import Asset

class AssetManager:
    def __init__(self):
        self.assets: List[Asset] = []

    def add_asset(self, asset: Asset):
        self.assets.append(asset)

    def remove_asset(self, asset_id: str) -> bool:
        for asset in self.assets:
            if asset.asset_id == asset_id:
                self.assets.remove(asset)
                return True
        return False

    def get_asset_by_id(self, asset_id: str) -> Optional[Asset]:
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        return None

    def assign_asset(self, asset_id: str, user: str) -> bool:
        for asset in self.assets:
            if asset.asset_id == asset_id:
                if asset.status == 'Available':
                    asset.assign_to_user(user)
                    return True
                else:
                    return False
        return False

    def unassign_asset(self, asset_id: str) -> bool:
        for asset in self.assets:
            if asset.asset_id == asset_id:
                if asset.status == 'Assigned':
                    asset.unassign()
                    return True
                else:
                    return False
        return False

    def get_available_assets(self) -> List[Asset]:
        return [asset for asset in self.assets if asset.status == 'Available']     

    def get_assigned_assets(self) -> List[Asset]:
        return [asset for asset in self.assets if asset.status == 'Assigned']

    def get_all_assets(self) -> List[Asset]:
        return self.assets
