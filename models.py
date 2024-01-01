from sqlalchemy import Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base

db = declarative_base()
meta = MetaData()


class User(db):
    __tablename__ = 'User_info'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    age = Column(String)
    datetime = Column(DateTime)
