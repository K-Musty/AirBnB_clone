#!/usr/bin/python3
from models.base_model import BaseModel

"""Class for
the user"""


class User(BaseModel):
    """User class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
