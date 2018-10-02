from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base,declared_attr
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import *
import os

DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_PORT = os.environ['DB_PORT']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']

db_string = DB_NAME+"://"+DB_USER+":"+DB_PASS+"@"+DB_HOST+":"+DB_PORT
db = create_engine(db_string, echo=True)
base = declarative_base()
Session = sessionmaker(db)
session = Session()
base.metadata.create_all(db)

class Users(base):
    __tablename__ = 'users'

    def __str__(self):
        # return str(self.__dict__)
        return { 'name': self.name, \
                'birthday': self.birthday, \
                'address': self.address, \
                'email': self.email }

    def __repr__(self):
        return self.name.replace(" ","_")

    @staticmethod
    def startengine():
        db_string = DB_NAME+"://"+DB_USER+":"+DB_PASS+"@"+DB_HOST+":"+DB_PORT
        db = create_engine(db_string)
        Session = sessionmaker(db)
        session = Session()
        base.metadata.create_all(db)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique = True, nullable=False)
    birthday = Column(DateTime)
    email = Column(String(50))
    address = Column(String(255))


    def __init__(self):
        self.startengine()

    # def to_json(self):
    #     return {'name': self.name, 'birthday': self.birthday, 'address': self.address, 'email': self.email}

    def retrive(self,name=None):
        if name is None:
            print('here')
            return session.query(Users).all()

        return session.query(Users) \
            .filter(Users.name == name.replace("_", " ")) \
            .first()

    def create(self,**kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.address = kwargs.get('address')
        self.birthday = kwargs.get('birthday')
        session.add(self)
        session.commit()
        Users.__print("created",kwargs.get('name'))

    def updateDb(self,key,**user):
        if key is None:
            return False

        pk1 = key.replace("_", " ")
        session.query(Users).filter(Users.name == pk1) \
                .update({"name": user.get('name'), \
                        "email": user.get('email'), \
                        "address": user.get('address'), \
                        "birthday": user.get('birthday')}, \
                synchronize_session=False)

        session.commit()
        Users.__print("updated",pk1)
        return True

    def delete(self,name):
        user = self.retrive(name)
        Users.__print("models.py","retrive")
        session.query(Users) \
            .filter(Users.name == name.replace("_"," ")) \
            .delete(synchronize_session=False)
        session.commit()
        Users.__print("deleted",name.replace("_", " "))
        return True

    def rollback(self):
        session.rollback()

    @staticmethod
    def __print(type, value):
        print("==========={0} [{1}]===========".format(type,value))
