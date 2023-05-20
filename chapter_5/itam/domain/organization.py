# define the Organization entity using Python's built-in dataclass decorator. The Organization entity has two attributes: id and name.

from dataclasses import dataclass

@dataclass
class Organization:
    id: int
    name: str

    def __post_init__(self):
        if self.id is None:
            raise TypeError("Id cannot be None")