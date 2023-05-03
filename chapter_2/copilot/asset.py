# Create a class named Asset
# Add the following attributes: 
# id, asset_type, manufacturer, model, purchase_date, purchase_price, warranty_end_date, location, and status. 
# The class should have a function named get_details returns a string which is the concatenation of all of the attributes.
# The class should have a function named to_dict that returns a dictionary of all of the attributes.

class Asset:
    def __init__(self):
        self.id = None
        self.asset_type = None
        self.manufacturer = None
        self.model = None
        self.purchase_date = None
        self.purchase_price = None
        self.warranty_end_date = None
        self.location = None
        self.status = None

    def get_details(self):
        return f"{self.id}, {self.asset_type}, {self.manufacturer}, {self.model}, {self.purchase_date}, {self.purchase_price}, {self.warranty_end_date}, {self.location}, {self.status}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "asset_type": self.asset_type,
            "manufacturer": self.manufacturer,
            "model": self.model,
            "purchase_date": self.purchase_date,
            "purchase_price": self.purchase_price,
            "warranty_end_date": self.warranty_end_date,
            "location": self.location,
            "status": self.status
        }