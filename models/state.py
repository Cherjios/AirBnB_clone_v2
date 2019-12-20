#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') is 'db':
        cities = relationship('City', backref='state')
    else:
        @property
        def cities(self):
            my_cities = []
            towns = models.storage.all('City')
            for kew, value in towns.tems():
                if value.state_id == self.id:
                    my_cities.append(value)
            return my_cities