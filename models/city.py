#!/usr/bin/python3
""" Module to get the BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City inherits from BaseModel"""

    name = ""
    state_id = ""
