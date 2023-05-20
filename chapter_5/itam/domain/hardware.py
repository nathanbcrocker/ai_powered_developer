# Define a class called Hardware, which is an instance of Asset. 
# The Hardware entity has the following attributes:
# - serial_number: str,
# - location: Location,
# - warranty_expiration_date: date,
# - notes: str
# - maintenance_schedules: List[MaintenanceSchedule]
# - warranty: Warranty
# - retirement_date: date
# - retirement_reason: str
# - usage_statistics: UsageStatistics
# - budget: Budget
# The attributes can be None and the class should have a constructor that takes all attributes as parameters.
# The attributes should be private and the class should have accessor methods for all attributes.

from datetime import datetime
from itam.domain.asset import Asset
from itam.domain.location import Location
from itam.domain.warranty import Warranty
from itam.domain.maintenance_schedule import MaintenanceSchedule
from itam.domain.usage_statistics import UsageStatistics
from itam.domain.budget import Budget

class Hardware(Asset):
    serial_number: str
    location: Location
    warranty_expiration_date: datetime
    notes: str
    maintenance_schedules: list[MaintenanceSchedule]
    warranty: Warranty
    retirement_date: datetime
    retirement_reason: str
    usage_statistics: UsageStatistics
    budget: Budget

    def get_serial_number(self) -> str:
        return self.serial_number

    def get_location(self) -> Location:
        return self.location

    def get_warranty_expiration_date(self) -> datetime:
        return self.warranty_expiration_date

    def get_notes(self) -> str:
        return self.notes

    def get_maintenance_schedules(self) -> list[MaintenanceSchedule]:
        return self.maintenance_schedules

    def get_warranty(self) -> Warranty:
        return self.warranty

    def get_retirement_date(self) -> datetime:
        return self.retirement_date

    def get_retirement_reason(self) -> str:
        return self.retirement_reason

    def get_usage_statistics(self) -> UsageStatistics:
        return self.usage_statistics

    def get_budget(self) -> Budget:
        return self.budget

