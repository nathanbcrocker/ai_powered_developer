# Create a class called User. 
# The User entity has the following attributes:
# - username: str, 
# - password: str,
# - roles: List[Role]
# none of the attributes can be None
# The User entity should have two methods: has_role() and has_role_by_name().

from dataclasses import dataclass
from typing import List
from itam.domain.role import Role

@dataclass
class User:
    username: str
    password: str
    roles: List[Role]

    def __post_init__(self):
        if self.username is None:
            raise TypeError("Username cannot be None")
        if self.password is None:
            raise TypeError("Password cannot be None")
        if self.roles is None:
            raise TypeError("Roles cannot be None")

    def has_role(self, role: Role) -> bool:
        return role in self.roles
    
    def has_role_by_name(self, role_name: str) -> bool:
        for role in self.roles:
            if role.name == role_name:
                return True
        return False