# Define the MaintenanceSchedule entity. It should have the following attributes: 
# - id: int, 
# - name: str, 
# - description: str, 
# - start_date: date, 
# - end_date: date, 
# - hardware : Hardware

from datetime import datetime
from dataclasses import dataclass

@dataclass
class MaintenanceSchedule:
    id: int
    name: str
    description: str
    start_date: datetime
    end_date: datetime

    def __post_init__(self):
        if self.id is None:
            raise TypeError("Id cannot be None")
        if self.name is None:
            raise TypeError("Name cannot be None")
        if self.description is None:
            raise TypeError("Description cannot be None")
        if self.start_date is None:
            raise TypeError("Start date cannot be None")
        if self.end_date is None:
            raise TypeError("End date cannot be None")