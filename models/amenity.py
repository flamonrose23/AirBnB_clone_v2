#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel):
    """amenity class"""
    __tablename__ = 'amenities'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                viewonly=False)
    else:
        name = ""
