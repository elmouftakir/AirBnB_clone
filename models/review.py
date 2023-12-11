#!/usr/bin/python3
""" Classe Review """

from models.base_model import BaseModel


class Review(BaseModel):
    """ classe attributes """
    place_id = ""
    user_id = ""
    text = ""
