#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.basemodel import BaseModel, Base
from sqlalchemy.exc import SQLAlchemyError
from os import getenv
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import scoped_session, sessionmaker
#from models.food import Food
from models.users import User
# from models.order import Order
from models.rider import Rider
#from models.restaurants import Restaurant
from dotenv import load_dotenv

load_dotenv()

classes = {"User": User, "Rider": Rider}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object
        """
        # The object URL is a string containing the information needed
        # to open a database connection.
        #url_object = URL.create(
        #    "mysql+mysqldb",
        #    user="app_user",
        #    password="food_pwd",
        #    host="localhost",
        #    database="food_App_db",
        #)
        try:
            user = getenv("FOOD_MYSQL_USER")
            password = getenv("FOOD_MYSQL_PWD")
            host = getenv("FOOD_MYSQL_HOST")
            db = getenv("FOOD_MYSQL_DB")
            env = getenv("FOOD_ENV")
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                          format(user,
                                                 password,
                                                 host,
                                                 db))
            self.reload()
            #self.__engine = create_engine(url_object, pool_pre_ping=True)  # pool_pre_ping tests connections before using them
            self.__engine.connect()
            if env == "test":
                Base.metadata.drop_all(self.__engine)
        except SQLAlchemyError as e:
            print("An error occurred while establishing the database connection:", str(e))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls == None or cls == classes[clss] or cls == clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute
        close session - stop using it"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count

