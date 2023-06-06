#!usr/bin/python3
"""Rider class"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, VARCHAR
import models


class Rider(BaseModel, Base):
    """ base class for all riders"""
    __tablename__ = 'riders'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    # image = Column(String(60), nullable=False)
    bike = Column(VARCHAR(60), nullable=False)
    number_plate = Column(VARCHAR(60), nullable=False)
    rating = Column(Float, nullable=True)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


