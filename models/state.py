#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from sqlalchemy import Column, String, Integer, ForeignKey
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship

from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ''

    @property
    def cities(self):
        "cities getter"
        city_list = []
        all_cities = models.storage, all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
            return city_list
