#!/usr/bin/python3
""" This module holds a class to manage storage """

from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review

objects = {
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class DBStorage:
    """ Class that manages storage """
    __engine = None
    __session = None

    def __init__(self):
        USER = getenv('HBNB_MYSQL_USER')
        PWD = getenv('HBNB_MYSQL_PWD')
        HOST = getenv('HBNB_MYSQL_HOST')
        DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            USER, PWD, HOST, DB), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        obj_dict = {}
        if cls is None:
            for val in objects.values():
                for o in self.__session.query(val):
                    key = o.__class__.__name__ + '.' + o.id
                    obj_dict[key] = o
        if cls in objects:
            for o in self.__session.query(objects[cls]):
                key = o.__class__.__name__ + '.' + o.id
                obj_dict[key] = o
        return obj_dict

    def new(self, obj):
        ''' Adds new object '''
        self.__session.add(obj)

    def save(self):
        ''' commits changes '''
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reloads the storage """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        SeSS = scoped_session(sess)
        self.__session = SeSS

    def close(self):
        """ Closes the session """
        self.__session.remove()
