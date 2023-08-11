#!/usr/bin/python3
""" Module to get the BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class User inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
