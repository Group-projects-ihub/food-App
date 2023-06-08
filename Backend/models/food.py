#!/usr/bin/python3

"""creates a class."""


from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, VARCHAR, INTEGER
from enum import Enum
from models.restaurants import Restaurant
# from enum import Enum  # for enum requirements in SQLAlchemy


class Food_Choices:
    # apply Enum in this calss to restrict the choices of food_type
    # choices = Enum('Food', 'Beverage')  # choices could be Food or Beverage only
    FOOD = 'Food' 
    Beverage = 'Beverage' 

class Food_Category_Choices:
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'


class Food(BaseModel, Base):
    """food class."""
    __tablename__ = 'food'
    # restaurant_id = Column(String(128), ForeignKey('restaurant.id'), nullable=False)
    quantity = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False)
    quantity = Column(String(128), nullable=False)
#     image_path = Column(String(256), nullable=True)
    description = Column(VARCHAR(255), nullable=False)
    food_category = Column(String(128), nullable=False)
    restaurant_id = Column(VARCHAR(255), ForeignKey('restaurants.id'), nullable=False) 
    # default=Food_Category_Choices.LUNCH, nullable=False)
    description = Column(String(512), nullable=False)
    # food_type = Column(Enum(Food_Choices), default=Food_Choices.FOOD, nullable=False)
    # food_category = Column(Enum(Food_Category_Choices), default=Food_Category_Choices.LUNCH, nullable=False)

