# Create a class called Role. 
# The Role entity has the following attributes:
# - id: int, 
# - name: str
# none of the attributes can be None

from dataclasses import dataclass

@dataclass
class Role:
    id: int
    name: str

    def __post_init__(self):
        if self.id is None:
            raise TypeError("Id cannot be None")
        if self.name is None:
            raise TypeError("Name cannot be None")