class Asset:
    def __init__(self, asset_id, asset_type, manufacturer, model, purchase_date, warranty_end_date, location):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.manufacturer = manufacturer
        self.model = model
        self.purchase_date = purchase_date
        self.warranty_end_date = warranty_end_date
        self.location = location
        self.assigned_to = None
        self.status = 'Available'

    def assign_to_user(self, user):
        self.assigned_to = user
        self.status = 'Assigned'

    def unassign(self):
        self.assigned_to = None
        self.status = 'Available'

    def get_details(self):
        details = f"Asset ID: {self.asset_id}\n"
        details += f"Type: {self.asset_type}\n"
        details += f"Manufacturer: {self.manufacturer}\n"
        details += f"Model: {self.model}\n"
        details += f"Purchase Date: {self.purchase_date}\n"
        details += f"Warranty End Date: {self.warranty_end_date}\n"
        details += f"Location: {self.location}\n"
        details += f"Assigned To: {self.assigned_to}\n"
        details += f"Status: {self.status}\n"
        return details
