from flask import Flask, request, jsonify
from asset import Asset
from asset_manager import AssetManager

app = Flask(__name__)
asset_manager = AssetManager()

# Add some example assets
asset_manager.add_asset(Asset('001', 'Laptop', 'Dell', 'Latitude E7470', '2021-01-01', '2024-01-01', 'New York'))
asset_manager.add_asset(Asset('002', 'Desktop', 'HP', 'EliteDesk 800 G5', '2021-02-01', '2024-02-01', 'San Francisco'))
asset_manager.add_asset(Asset('003', 'Server', 'Dell', 'PowerEdge R740', '2021-03-01', '2024-03-01', 'London'))


# Get all assets
@app.route('/assets', methods=['GET'])
def get_assets():
    assets = [asset.__dict__ for asset in asset_manager.assets]
    return jsonify({'assets': assets})


# Get an asset by ID
@app.route('/assets/<string:asset_id>', methods=['GET'])
def get_asset(asset_id):
    asset = asset_manager.get_asset_by_id(asset_id)
    if asset:
        return jsonify(asset.__dict__)
    else:
        return jsonify({'error': 'Asset not found'})


# Add a new asset
@app.route('/assets', methods=['POST'])
def add_asset():
    asset_data = request.get_json()
    asset = Asset(asset_data['asset_id'], asset_data['asset_type'], asset_data['manufacturer'], asset_data['model'],
                  asset_data['purchase_date'], asset_data['warranty_end_date'], asset_data['location'])
    asset_manager.add_asset(asset)
    return jsonify({'message': 'Asset added successfully'})


# Update an existing asset
@app.route('/assets/<string:asset_id>', methods=['PUT'])
def update_asset(asset_id):
    asset_data = request.get_json()
    asset = asset_manager.get_asset_by_id(asset_id)
    if asset:
        asset.asset_type = asset_data['asset_type']
        asset.manufacturer = asset_data['manufacturer']
        asset.model = asset_data['model']
        asset.purchase_date = asset_data['purchase_date']
        asset.warranty_end_date = asset_data['warranty_end_date']
        asset.location = asset_data['location']
        return jsonify({'message': 'Asset updated successfully'})
    else:
        return jsonify({'error': 'Asset not found'})


# Delete an asset by ID
@app.route('/assets/<string:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    success = asset_manager.remove_asset(asset_id)
    if success:
        return jsonify({'message': 'Asset deleted successfully'})
    else:
        return jsonify({'error': 'Asset not found'})


# Assign an asset to a user
@app.route('/assets/<string:asset_id>/assign', methods=['PUT'])
def assign_asset(asset_id):
    user_data = request.get_json()
    success = asset_manager.assign_asset(asset_id, user_data['user'])
    if success:
        return jsonify({'message': 'Asset assigned successfully'})
    else:
        return jsonify({'error': 'Asset not available or not found'})


# Unassign an asset from its user
@app.route('/assets/<string:asset_id>/unassign', methods=['PUT'])
def unassign_asset(asset_id):
    success = asset_manager.unassign_asset(asset_id)
    if success:
        return jsonify({'message': 'Asset unassigned successfully'})
    else:
        return jsonify({'error': 'Asset not assigned or not found'})


if __name__ == '__main__':
    app.run(debug=True)
