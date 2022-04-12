#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""
