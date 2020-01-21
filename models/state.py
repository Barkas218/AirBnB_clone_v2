#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import environ
from models.city import City

class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if environ['HBNB_TYPE_STORAGE'] != 'db':
        @property
        def cities(self):
            '''FileStorage relationship between State and City '''
            cities = models.storage.all(City)
            cities_relation = []

            for city in cities.values():
                if city.state_id == self.id:
                    cities_relation.append(city)
            return cities_relation
