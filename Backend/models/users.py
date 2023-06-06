#!usr/bin/python3

""" User class for the Food app"""

from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, VARCHAR, INTEGER
import models

class User(BaseModel, Base):
    """User class for the Food app"""

    __tablename__ = "users"
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(VARCHAR(255), nullable=False)
    email = Column(String(128), nullable=False)
    role = Column(VARCHAR(255), nullable=False)
    password = Column(VARCHAR(128), nullable=False)
    phone_number = Column(INTEGER(128), nullable=False)
    id_number = Column(INTEGER(128), nullable=False)
    # location = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initialize the user"""
        super().__init__(*args, **kwargs)
