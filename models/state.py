#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """

    if (storage_type == 'db'):
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            return [
                city for city in storage.all(City).values()
                if city.state_id == self.id
            ]

    def __init__(self, *args, **kwargs):
        """Class Initilization"""

        super().__init__(*args, **kwargs)
