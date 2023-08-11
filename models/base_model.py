#!/usr/bin/python3
""" Module to take care of the initialization, \
    serialization and deserialization of your future instances"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """Class BaseModel defines all common \
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'updated_at' or key == 'created_at':
                        self.__dict__[key] = datetime.fromisoformat(value)
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at \
        with the current datetime"""

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values \
        of __dict__ of the instance"""

        dictionary = dict(self.__dict__)
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = \
            datetime.isoformat(dictionary.get('created_at'))
        dictionary['updated_at'] = \
            datetime.isoformat(dictionary.get('updated_at'))
        return dictionary
