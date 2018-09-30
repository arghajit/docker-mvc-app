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

    # @declared_attr
    # def users(cls):
    #     return relationship('users')



        #  parameretized constructor
    # def __init__(self):
        # self.name = kwargs.get('name')
        # self.email = kwargs.get('email')
        # self.address = kwargs.get('address')
        # self.birthday = kwargs.get('birthday')


    # def to_json(self):
    #     return {'name': self.name, 'birthday': self.birthday, 'address': self.address, 'email': self.email}
    #
    # @classmethod
    # def from_json(cls, json):
    #     return User(json['user'])
    #
    # title = Column(String, primary_key=True)
    # director = Column(String)
    # year = Column(String)
    def retrive(self,name=None):
        if name is None:
            return session.query(Users).all()

        return session.query(Users) \
            .filter(Users.name == name.replace("_", " ")) \
            .first()


        # print("===========models.py/retrieve===========")
        # items = session.query(Users).filter_by(name = name.replace("_"," "))
        # for item in items:
        #     print(item)
        # return items

    def create(self,**kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.address = kwargs.get('address')
        self.birthday = kwargs.get('birthday')
        session.add(self)
        session.commit()
        Users.__print("created",kwargs.get('name'))
        # return True

    def updateDb(self,key,**user):
        if key is None:
        # if len(args) < 1:
            return False

        # print("==========={0}".format(arg[0]))
        pk1 = key.replace("_", " ")
        # print("=key=========={0}".format(pk1))
        # pk = pk1
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
        # name = name.replace("_"," ")
        user = self.retrive(name)
        Users.__print("models.py","retrive")
        # print(user)
        # session.delete(user)
        session.query(Users) \
            .filter(Users.name == name.replace("_"," ")) \
            .delete(synchronize_session=False)
        session.commit()
        Users.__print("deleted",name.replace("_", " "))
        return True

    def rollback(self):
        session.rollback()
# Read
# films = session.query(Film)
# for film in films:
#     print(film.title)

# Update
# doctor_strange.title = "Some2016Film"
# session.commit()



    @staticmethod
    def __print(type, value):
        print("==========={0} [{1}]===========".format(type,value))

# Delete
# session.delete(doctor_strange)
# session.commit()
