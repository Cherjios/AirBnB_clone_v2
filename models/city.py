#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
<<<<<<< HEAD

    __tablename__ = 'cities'

    name = Column(String(128),
                  nullable=False)

    state_id = Column(String(60),
                      ForeignKey('states.id'),
                      nullable=False)

    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
=======
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities")
>>>>>>> bc30c199a8c8d4557d14250745ba70a472702197
