# Create a class called AssetManager that will allow us to store and retrieve assets.

class AssetManager:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def get_assets(self):
        return self.assets

    def get_asset(self, asset_id):
        for asset in self.assets:
            if asset.id == asset_id:
                return asset
        return None

    def update_asset(self, asset_id, asset):
        for index, asset in enumerate(self.assets):
            if asset.id == asset_id:
                self.assets[index] = asset
                return True
        return False

    def delete_asset(self, asset_id):
        for index, asset in enumerate(self.assets):
            if asset.id == asset_id:
                del self.assets[index]
                return True
        return False