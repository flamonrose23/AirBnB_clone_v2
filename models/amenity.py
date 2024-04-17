#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


<<<<<<< HEAD
class Amenity(BaseModel):
    """amenity class"""
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                viewonly=False)
=======
class Amenity(BaseModel, Base):
    """
    Amenity class
    """
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
>>>>>>> 2357cb0e1bb4ca905f3be1331d61d3062fb7e892
    else:
        name = ""
