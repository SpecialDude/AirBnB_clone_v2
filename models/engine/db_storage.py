#!/usr/bin/python3

"""The Database Storage Engine"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

all_models = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "User": User
}


class DBStorage:
    """The database storage Engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Class instantiation"""

        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')

        url = "mysql://{}:{}@{}/{}".format(
            HBNB_MYSQL_USER,
            HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST,
            HBNB_MYSQL_DB
        )

        self.__engine = create_engine(url, pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """Query on the current database session"""

        data = {}

        for model_name in all_models:
            mmodel = all_models[model_name]
            if cls is None or cls is mmodel or cls is model_name:
                objects = self.__session.query(mmodel).all()

                for obj in objects:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    data[key] = obj
        return data

    def new(self, obj):
        """Add a new object to the current session"""

        self.__session.add(obj)

    def save(self):
        """Commit all changes in the current session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current session"""

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Load up data from the database"""

        Base.metadata.create_all(self.__engine)
        _session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(_session)
