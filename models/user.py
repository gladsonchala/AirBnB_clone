#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user in the system"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
