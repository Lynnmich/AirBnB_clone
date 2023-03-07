"""Base Model Class
   The Base class of all other model
"""
from copy import copy
import datetime
import uuid


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """

    def __init__(self):
        """Called when a BaseModel is created"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = copy(self.created_at)

