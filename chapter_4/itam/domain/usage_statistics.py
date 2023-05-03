#    Define a class claaed UsageStatistics with the following attributes:
#        -id: int
#        -start_date: date
#        -end_date: date
#        -total_up_time: float
#        -total_down_time: float
#        -average_up_time: float
#        -average_down_time: float
#    and with the following methods:
#        +__init__(self, hardware: Hardware, start_date: date, end_date: date, total_up_time: float, total_down_time: float, average_up_time: float, average_down_time: float)
#        +get_id(self) -> int
#        +get_start_date(self) -> date
#        +get_end_date(self) -> date
#        +get_total_up_time(self) -> float
#        +get_total_down_time(self) -> float
#        +get_average_up_time(self) -> float
#        +get_average_down_time(self) -> float
#        +set_start_date(self, start_date: date)
#        +set_end_date(self, end_date: date)
#        +set_total_up_time(self, total_up_time: float)
#        +set_total_down_time(self, total_down_time: float)
#        +set_average_up_time(self, average_up_time: float)
#        +set_average_down_time(self, average_down_time: float)
#    }

from datetime import datetime
from dataclasses import dataclass

@dataclass
class UsageStatistics:
    id: int
    start_date: datetime
    end_date: datetime
    total_up_time: float
    total_down_time: float
    average_up_time: float
    average_down_time: float

    def __post_init__(self):
        if self.id is None:
            raise TypeError("Id cannot be None")
        if self.start_date is None:
            raise TypeError("Start date cannot be None")
        if self.end_date is None:
            raise TypeError("End date cannot be None")
        if self.total_up_time is None:
            raise TypeError("Total up time cannot be None")
        if self.total_down_time is None:
            raise TypeError("Total down time cannot be None")
        if self.average_up_time is None:
            raise TypeError("Average up time cannot be None")
        if self.average_down_time is None:
            raise TypeError("Average down time cannot be None")

    def get_id(self):
        return self.id

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_total_up_time(self):
        return self.total_up_time

    def get_total_down_time(self):
        return self.total_down_time

    def get_average_up_time(self):
        return self.average_up_time

    def get_average_down_time(self):
        return self.average_down_time

    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_total_up_time(self, total_up_time):
        self.total_up_time = total_up_time

    def set_total_down_time(self, total_down_time):
        self.total_down_time = total_down_time

    def set_average_up_time(self, average_up_time):
        self.average_up_time = average_up_time

    def set_average_down_time(self, average_down_time):
        self.average_down_time = average_down_time