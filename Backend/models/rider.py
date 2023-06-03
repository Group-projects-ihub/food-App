#!usr/bin/python3
"""Rider class"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Rider(BaseModel, Base):
    """ base class for all riders"""
    
    __tablename__ = 'riders'
    phone_number = Column(String(60), nullable=False)
    name = Column(String(60), nullable=False)
    age = Column(Integer, nullable=False)
    image = Column(String(60), nullable=False)
    country = Column(String(60), nullable=False)
    bike = Column(String(60), nullable=False)
    rating = Column(Float, nullable=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


