#!/usr/bin/python3
""" Place class """

from models.base_model import BaseModel


class Place(BaseModel):
    """ class constructor """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
<<<<<<< HEAD

=======
>>>>>>> 64151464dff7917d410f7d25e2d2c4a9ec52fb80
