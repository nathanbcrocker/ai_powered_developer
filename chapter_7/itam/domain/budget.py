# create a class called Budget
# with the following attributes:
# - id: int, name: str, department_id: int, amount: float, start_date: datetime, end_date: datetime
# id cannot be nil
# deparment cannot be nil
# amount cannot be nil
# automatically generates special methods for a class that are commonly used for data objects

from datetime import datetime
from dataclasses import dataclass

@dataclass
class Budget:
    id: int
    name: str
    department_id: int
    amount: float
    start_date: datetime
    end_date: datetime

    def __post_init__(self):
        if self.id is None:
            raise TypeError("Id cannot be None")
        if self.department_id is None:
            raise TypeError("Department cannot be None")
        if self.amount is None:
            raise TypeError("Amount cannot be None")