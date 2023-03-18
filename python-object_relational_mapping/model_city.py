#!/usr/bin/python3
"""
create table city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """table declaration"""
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128))
    state_id = Column(Integer,
                      ForeignKey('states.id'))
    state = relationship('State')
