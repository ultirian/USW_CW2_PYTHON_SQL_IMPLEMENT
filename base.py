# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the MYSQL Engine using MySQL Connector/Python
engine = create_engine('mysql+mysqlconnector://testuser:Joe!25145309@localhost:3306/user', echo=False)

# Create a Session
Session = sessionmaker(bind=engine)

# define and create table
Base = declarative_base()


def create_session():
    session = Session()
    return session
