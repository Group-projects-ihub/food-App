from datetime import datetime
from sqlalchemy import Column, String, DateTime

from models.basemodel import BaseModel, Base


class Restaurant(BaseModel, Base):
    """Model class for a restaurant"""

    name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    cuisine = Column(String(255), nullable=False)

    def __init__(self, name, address, cuisine, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.address = address
        self.cuisine = cuisine

    def __str__(self):
        return "[{:s}] ({:s}) Name: {:s}, Address: {:s}, Cuisine: {:s}".format(
            self.__class__.__name__, self.id, self.name, self.address, self.cuisine
        )

