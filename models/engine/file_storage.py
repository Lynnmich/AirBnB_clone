#!/usr/bin/python3
"""This module represents file storage class"""
import json


class FileStorage():
    """This class serializes instances
    to JSON file and deserializes JSON file to instances"""

    __file_path = ""
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(
            obj.__class__.name, id)] = obj

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path)"""

        dict_ob = FileStorage.__objects
        objTodict = {key: dict_ob[key].to_dict() for key in dict_ob.keys()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(objTodict)

    def reload(self):
        """deserializes the JSON file to __objects """
        try:
            with open(FileStorage.__file_path) as f:
                loads_obj = json.load(f)
                for obj in loads_obj.values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
