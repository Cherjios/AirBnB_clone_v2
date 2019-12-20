#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
import models



class DBStorage:

    __engine = None
    __session = None

    def __init__(self):

        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database)), pool_pre_ping=True)

        if getenv(HBNB_ENV) == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        dict = {}
        if cls == None:
            lineup = self.__session.query(User).all()
            lineup += self.__session.query(State).all()
            lineup += self.__session.query(City).all()
            lineup += self.__session.query(Amenity).all()
            lineup += self.__session.query(Place).all()
            lineup += self.__session.query(Review).all()
        else:
            lineup = self.__session.query(eval(cls)).all()

        for line in lineup:
            line = type(obj).__name__ + '.' + obj.id
            dict[line] = obj

        return dict

    def new(self, obj):
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

"""ARE WE NOW SUPPOSED TO CLOSE THE SESSION?"""
"""IF YES, DO WE CREATE A SEPARATE METHOD OR ADD SELF.__SESSION.CLOSE() TO RELOAD? DELETE?"""
