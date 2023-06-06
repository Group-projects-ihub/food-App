from datetime import datetime
from sqlalchemy import Column, String, VARCHAR

from models.basemodel import BaseModel, Base


class Restaurant(BaseModel, Base):
    """Model class for a restaurant"""

    __tablename__ = "restaurants"
    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    description = Column(VARCHAR(255), nullable=False)
    rating = Column(VARCHAR(255), nullable=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def __str__(self):
    #     return "[{:s}] ({:s}) Name: {:s}, Address: {:s}, Cuisine: {:s}".format(
    #         self.__class__.__name__, self.id, self.name, self.address, self.cuisine
    #     )
