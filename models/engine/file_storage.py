#!/usr/bin/python3
""" serializes instances to a JSON file and \
    deserializes JSON file to instances:"""
import json


class FileStorage:
    """serializes instances to a JSON file \
        and deserializes JSON file to instances:"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w", encoding='utf-8') as f:
            dic = {}
            for key, value in self.__objects.items():
                dic[key] = value.to_dict()
            json.dump(dic, f)

    def reload(self):
        """"deserializes the JSON file to __objects ; \
            otherwise, do nothing"""

        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review
        from models.place import Place

        new_list = {
                    "User": User, "BaseModel": BaseModel, "City": City,
                    "State": State, "Amenity": Amenity, "Review": Review,
                    "Place": Place
                }
        try:
            with open(self.__file_path, "r", encoding='utf-8') as f:
                dic = json.load(f)
                for value in dic.values():
                    self.new(new_list[value['__class__']](**value))
        except FileNotFoundError:
            pass
