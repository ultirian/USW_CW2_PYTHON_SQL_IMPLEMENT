# coding=utf-8
# Libraries
import secrets
import string
import pyinputplus as pyin
from user import User
from base import Session, engine, Base, create_session
from password_strength import PasswordPolicy
from password_strength import PasswordStats


# Functions
def add_user():
    # Call create_session() func to local object
    session = create_session()
    # Set user terms
    username_l = user_setter()
    firstname_l = firstname_setter()
    lastname_l = lastname_setter()
    password_l = password_setter()
    pin_o = generate_pin()
    usertype_l, is_admin_l, is_lecturer_l, is_student_l = usertype_setter()
    # Add a User
    new_user = User(username=username_l, firstname=firstname_l.capitalize(), lastname=lastname_l.capitalize(),
                    password=password_l, usertype=usertype_l, pin=pin_o, is_admin=is_admin_l,
                    is_lecturer=is_lecturer_l, is_student=is_student_l)

    session.add(new_user)
    session.commit()
    session.close()


def generate_pin():
    number = string.digits
    _pin = ''.join(secrets.choice(number) for i in range(4))
    print(f"Pin: {_pin}")
    return _pin


def firstname_setter():
    while True:
        firstname_l = pyin.inputStr("Insert Firstname: ")
        if firstname_l.isalpha() or firstname_l.isalpha():
            break
        print("Please enter characters A-Z only")

    return firstname_l


def lastname_setter():
    while True:
        lastname_l = pyin.inputStr("Insert Lastname: ")
        if lastname_l.isalpha() or lastname_l.isalpha():
            break
        print("Please enter characters A-Z only")

    return lastname_l


def password_setter():
    # set password policy TODO
    policy = PasswordPolicy.from_names(
        length=12,  # min length: 8
        uppercase=2,  # need min. 2 uppercase letters
        numbers=4,  # need min. 2 digits
        special=2,  # need min. 2 special characters
        nonletters=4,  # need min. 2 non-letter characters (digits, specials, anything)
    )

    password_l = pyin.inputStr("Insert Password: ")
    stats = PasswordStats(password_l)

    while stats.strength() < 0.7:
        stats = PasswordStats(password_l)
        if stats.strength() < 0.7:
            print("Weak Password")
            password_l = pyin.inputStr("Insert Password: ")
        elif stats.strength() >= 0.7:
            print("Strong Password")
            break

    print(policy.test(password_l))
    return password_l


def usertype_setter():
    usertype_l = pyin.inputChoice(['1', '2', '3'], prompt="Press 1 for Admin | 2 For Lecturer | 3 For Student: ")

    is_admin_l = False
    is_lecturer_l = False
    is_student_l = False

    if usertype_l == "1":
        is_admin_l = True
    elif usertype_l == "2":
        is_lecturer_l = True
    elif usertype_l == "3":
        is_student_l = True
    else:
        print("Incorrect Input")

    return usertype_l, is_admin_l, is_lecturer_l, is_student_l


def user_setter():
    # User Inputs
    username_l = pyin.inputStr("Insert Username: ")
    # Test for duplicate username queries database for username returning boolean.
    while test_duplicate_user(username_l):
        username_l = pyin.inputStr("Please Re-insert Username: ")

    return username_l


def query_user():
    # Call create_session() func to local object
    session = create_session()
    # Query the user
    username_input_local = pyin.inputStr(" Insert Search User: ")
    our_user = session.query(User).filter_by(username=username_input_local).first()

    if our_user:
        print("Username Found")
        print('\nOur User:')
        print(our_user)
    else:
        print("Username Not Found")
        print('\nOur User:')
        print(our_user)

    session.close()


def test_duplicate_user(username_in):
    # Call create_session() func to local object
    session = create_session()
    # Query the user
    our_user = session.query(User).filter_by(username=username_in).first()
    if our_user:
        print("Duplicate Username Found")
        return True
    else:
        print("Username Available")
        return False


Base.metadata.create_all(engine)
