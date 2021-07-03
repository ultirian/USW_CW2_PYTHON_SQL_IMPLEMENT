# coding=utf-8
# Libraries
from sqlalchemy import Column, String, Integer, Boolean, Table, ForeignKey

from base import Base

# Classes
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=50))
    firstname = Column(String(length=50))
    lastname = Column(String(length=50))
    password = Column(String(length=50))
    usertype = Column(Integer())
    pin = Column(String(length=4))
    is_admin = Column(Boolean())
    is_lecturer = Column(Boolean())
    is_student = Column(Boolean())

    def __init__(self, username, firstname, lastname, password,usertype, pin, is_admin, is_lecturer, is_student):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        self.usertype = usertype
        self.pin = pin
        self.is_admin = is_admin
        self.is_lecturer = is_lecturer
        self.is_student = is_student

    # Returns a string representation of the object.
    def __repr__(self):
        return "<User(username='{0}', firstname='{1}', lastname='{2}', password='{3}', " \
               "usertype='{4}', pin='{5}', is_admin='{6}, is_lecturer='{7}', is_student='{8}')>" \
            .format(self.username, self.firstname, self.lastname, self.password,
                    self.usertype, self.pin, self.is_admin, self.is_lecturer, self.is_student)