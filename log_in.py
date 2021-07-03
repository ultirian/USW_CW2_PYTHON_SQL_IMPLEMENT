# coding=utf-8
# Libraries
import pyinputplus as pyin
from user import User
from base import Session, engine, Base, create_session
from sqlalchemy.orm.exc import NoResultFound
import pprint


# Functions


def query_user():
    # Call create_session() func to local object
    session = create_session()
    # Query the user
    username_input_local = pyin.inputStr(" Insert Search User: ")
    our_user = session.query(User).filter_by(username=username_input_local).first()
    if our_user:
        print("Username Found")
        print('\nOur User:')
        print("Username: ", our_user.username, "Firstname: ", our_user.firstname)
    else:
        print("Username Not Found")
        print('\nOur User:')
        print(our_user)

    session.close()


def log_in_user():
    check_username_match()


def check_password_match(user_obj):

    print(user_obj.password)
    pwd_in = pyin.inputStr("Insert Password: ")
    if user_obj.password == pwd_in:
        print("Password OK!")
        return True
    else:
        print("BAD PASSWORD!")
        return False


def check_username_match():
    session = create_session()
    # User Inputs
    username_l = pyin.inputStr("Insert Username: ")
    our_user = session.query(User).filter(User.username == username_l).one()
    # Creating object
    user_obj = User(username=our_user.username,
                    firstname=our_user.firstname,
                    lastname=our_user.lastname,
                    password=our_user.password,
                    usertype=our_user.usertype,
                    pin=our_user.pin,
                    is_admin=our_user.is_admin,
                    is_lecturer=our_user.is_lecturer,
                    is_student=our_user.is_student)
    try:
        if our_user:
            print("Username Found")
            # debugging
            print("Username: ", our_user.username, "Firstname: ", our_user.firstname)
            if check_password_match(user_obj):
                print("YOUR LOGGED IN NICE:")
        else:
            print("Username Not Found")
            print('\nOur User:')
            print(our_user)
    except NoResultFound as e:
        print(e)


def populate_login_object():
    pass
