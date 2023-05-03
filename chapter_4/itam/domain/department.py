# define a class called Department, using Python's built-in dataclass decorator. 
# The Department entity has two attributes: id: int, name: str.

from dataclasses import dataclass

@dataclass
class Department:
    id: int
    name: str