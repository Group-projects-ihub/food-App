#!/usr/bin/python3

"""creates a class."""


from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, VARCHAR, INTEGER
from enum import Enum


class Food_Choices(Enum):
    FOOD = 'Food'
    Beverage = 'Beverage'

class Food_Category_Choices(Enum):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'


class Food(BaseModel, Base):
    """food class."""
    __tablename__ = 'food'
    name = Column(String(128), nullable=False)
    quantity = Column(String(128), nullable=False)
    image_path = Column(String(256), nullable=True)
    description = Column(VARCHAR(255), nullable=False)
    food_category = Column(String(128), nullable=False)
    restaurant_id = Column(INTEGER(128), ForeignKey(
        'restaurant.id'), nullable=False)  # restaurant_id is the foreign key
    # default=Food_Category_Choices.LUNCH, nullable=False)

