#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from models import storage_type

if type_of_storage == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
            Column('place_id', String(60),
                ForeignKey('places.id'),
                primary_key=True,
                nullable=False),
            Column('amenity_id', String(60),
                ForeignKey('amenities.id'),
                primary_key=True,
                nullable=False)
            )

class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    if type_of_storage == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longtitude = Column(Float, nullable=False)
        reviews = relationship('Review', backref='place',
                cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                viewonly=False, backref='place_amenities')
    else:
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

        @property
        def reviews(self):
            """list of review instances with place id"""
            from models import storage
            all_reviws = storage.all(Review)
            rev_list = []
            for reviw in all_reviws.values():
                if reviw.place_id == self.id:
                    rev_list.append(reviw)
            return rev_list

        @property
        def amenities(self):
            """list of amenities"""
            from models import storage
            all_amenitys = storage.all(Amenity)
            amen_list = []
            for ament in all_amenitys.values():
                if ament.id in self.amenity_ids:
                    amen_list.append(ament)
            return amen_list

        @amenities.setter
        def amenities(self):
            """adding amenity.id to amenity_ids"""
            if obj is not None:
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
