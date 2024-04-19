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
    """ Representation class of State """
    __tablename__ == 'states'
    if type_of_storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                cascade='all, delete, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        """returning list of City instances with state_id"""
        from models import storage
        related_cities = []
        cities = storage.all(City)
        for city in cities.value():
            if city.state_id == self.id:
                related_cities.append(city)
        return related_cities
