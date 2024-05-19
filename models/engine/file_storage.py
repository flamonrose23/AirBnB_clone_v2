#!/usr/bin/python3
"""
Defining the module to manage FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """
    Serializing instances to JSON file & deserializing back to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returning dictionary in storage __objects
        """
        if cls is not None:
            nw_dict = {}
            for key, value in self.__objects.itms():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    nw_dict[key] = value
            return nw_dict
        return self.__objects

    def new(self, obj):
        """
        Adding new sets in __objects to storage with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Saving __objects to the JSON file (path: __file_path)
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """
        Deserializing JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deleting obj from __objects if it’s inside
        """
        if obj is not None:
            objct_key = obj.__class__.__name__ + '.' + obj.id
            if objct_key in self.__objects:
                del self.__objects[objct_key]

    def close(self):
        """
        calling reload() method for deserializing JSON file to objects
        """
        self.reload()
