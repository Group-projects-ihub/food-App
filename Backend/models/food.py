#!/usr/bin/python3

"""creates a class."""


from model.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
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
    restaurant_id = Column(String(128), ForeignKey('restaurant.id'), nullable=False)
    quantity = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=False)
    food_type = Column(Enum(Food_Choices), default=Food_Choices.FOOD, nullable=False)
    food_category = Column(Enum(Food_Category_Choices), default=Food_Category_Choices.LUNCH, nullable=False)

