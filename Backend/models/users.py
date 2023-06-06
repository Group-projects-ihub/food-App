#!usr/bin/python3

""" User class for the Food app"""

from models.basemodel import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
import models

class User(BaseModel, Base):
    """User class for the Food app"""

    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    location = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initialize the user"""
        super().__init__(*args, **kwargs)
        