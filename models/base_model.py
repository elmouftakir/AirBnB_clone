#!/usr/bin/python3
""" AirBnb project - BaseModel class """

import uuid
from datetime import datetime
import models
import copy


class BaseModel:
    """ This class defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ method constructor """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == "created_at":
                    self.created_at = datetime.strptime(value, form)
                    continue
