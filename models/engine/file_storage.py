"""This module represents file storage class"""


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
        FileStorage.__objects[obj.id] = obj
        