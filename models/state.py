#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship(
        'City',
        cascade='all, delete, delete-orphan'
        back_populates='state'
    )

    @property
    def cities(self):
        return cities
