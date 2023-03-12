#!/usr/bin/python3
"""This module represents file storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """This class serializes instances
    to JSON file and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "."
                              + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path)"""

        dict_ob = FileStorage.__objects
        objTodict = {key: dict_ob[key].to_dict() for key in dict_ob.keys()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(objTodict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                loads_obj = json.load(f)
                for obj in loads_obj.values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
        except json.JSONDecodeError:
            return

    def default(self, arg):
        """The default method"""
        arg_dict = {
            "all": self.do_all
        }
        nb_args = arg.split(".")

        if not len(nb_args):
            return super().default(arg)

        cls_name = nb_args[0]
        cmd_ = nb_args[1]

        if ("(" not in cmd_):
            return super().default(arg)

        tab_args = cmd_.split("(")

        if not len(tab_args):
            return super().default(arg)

        cmd_ = tab_args[0]

        if ")" not in tab_args[1]:
            return super().default(arg)

        s_arg = tab_args[1].replace(")", "")

        if "," in tab_args[1]:
            s_arg = s_arg.replace(",", "")

        cls_name = cls_name + " " + s_arg

        if cmd_ in arg_dict.keys():
            arg_dict[cmd_](cls_name)
            return

        return super().default(arg)