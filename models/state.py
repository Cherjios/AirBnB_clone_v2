#!/usr/bin/python3
"""This is the state class"""

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              cascade="all, delete-orphan",
                              backref="state")
    elif getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            l = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    l.append(city)
            return l
