class AssetManager:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def remove_asset(self, asset_id):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                self.assets.remove(asset)
                return True
        return False

    def get_asset_by_id(self, asset_id):
        for asset in self.assets:
            if asset.asset_id == asset_id:
                return asset
        return None

    def assign_asset(self, asset_id, user):
        asset = self.get_asset_by_id(asset_id)
        if asset and asset.status == 'Available':
            asset.assign_to_user(user)
            return True
        return False

    def unassign_asset(self, asset_id):
        asset = self.get_asset_by_id(asset_id)
        if asset and asset.status == 'Assigned':
            asset.unassign()
            return True
        return False

    def get_available_assets(self):
        return [asset for asset in self.assets if asset.status == 'Available']

    def get_assigned_assets(self):
        return [asset for asset in self.assets if asset.status == 'Assigned']
