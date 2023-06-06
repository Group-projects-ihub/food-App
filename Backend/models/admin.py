#!usr/bin/python3

"""creates admin that inherits user id class."""

from models.users import User
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, VARCHAR
from sqlalchemy.orm import relationship


class Admin(BaseModel, Base):
    """ admin class"""
    
    __tablename__ = 'admin'
    admin_id = Column(String(128), ForeignKey('users.id'), nullable=False)
    position = Column(VARCHAR(128), nullable=False)
    
    def __init__(self, *args, **kwargs):
        """initialize admin from BaseModel"""
        super().__init__(*args, **kwargs)