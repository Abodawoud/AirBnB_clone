#!/usr/bin/python3
""" Module to get the BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
