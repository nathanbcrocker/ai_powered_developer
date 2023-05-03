from typing import Optional

class Asset():
    def __init__(self, asset_id: str, asset_type: str, manufacturer: str, model: str, purchase_date: str, warranty_end_date: str, location: str):
        self.asset_id = asset_id
        self.asset_type = asset_type
        self.manufacturer = manufacturer
        self.model = model
        self.purchase_date = purchase_date
        self.warranty_end_date = warranty_end_date
        self.location = location
        self.assigned_to: Optional[str] = None
        self.status: str = 'Available'

    def assign_to_user(self, user: str):
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

    def to_dict(self):
        return {
            "asset_id": self.asset_id,
            "asset_type": self.asset_type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "purchase_date": self.purchase_date,
            "warranty_end_date": self.warranty_end_date,
            "location": self.location,
            "assigned_to": self.assigned_to,
            "status": self.status
        }