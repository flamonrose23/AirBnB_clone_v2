#!/usr/bin/python3

""" Defining State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Foreignkey
from os import getenv


class State(BaseModel, Base):
    """
    Representation of state
    """
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        Initializing state
        """
        super().__init__(*args, **kwargs)

    if models.storage_t != "db":
        @property
        def cities(self):
            """
            Gettering for list of city instances related t state
            """
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
