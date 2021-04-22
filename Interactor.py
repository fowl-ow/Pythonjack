import json
import re
from yes_no import yes, no
from getpass import getpass
from passlib.hash import bcrypt
from Database import Database
import forbidden_passwd
import forbidden_names


db = Database()


def get_name(text="", login=False):
    name = get_input(text)
    if not name_valid(name):
        print("Your name may only contain alphanumeric characters,\nand must be between 3 and 12 characters long.")
        if name_forbidden():
            print("Name forbidden.")
        elif not login:
            if get_decision("Are you happy with: {}?".format(name)):
                return name
    return


def name_valid(name):
    if re.match('^\w+$', name) and 2 < len(name) < 13:
        return True
    else:
        return False


def name_forbidden(name):
    for forbidden in forbidden_names.names:
        if name.lower() == forbidden:
            return True
        else:
            return False


def get_input(text=""):
    return check_exit(input(text))


def check_exit(text):
    if text.lower() == "quit":
        if get_decision("Are you sure?"):
            quit()
    return text


def check_back(text):
    if text.lower() == "back":
        return True
    else:
        False


def get_decision(text):
    while True:
        temp = str.lower(get_input(text + "\n"))
        check_exit(temp)
        for synonym in yes:
            if temp == synonym: return True
        for synonym in no:
            if temp == synonym: return False
        print("Sorry I didn't catch that.")


def get_int():
    while True:
        string = get_input()
        if not string.isdecimal():
            print("You may only enter integers.")
        else:
            return int(string)


def set_passwd():
    print("Please enter a strong password.")
    passwd = bcrypt.hash(getpass())
    if valid_passwd(passwd):
        print("Please confirm your password.")
        if bcrypt.verify(getpass(), passwd):
            return passwd
        else:
            print("Entered passwords don't match.")
    else:
        print("Password not valid.")


def get_passwd():
    print("Please enter the password.")
    passwd = getpass()

def password_verified(name, passwd):
    hash = db.get_user_password(name)
    return bcrypt.verify(passwd, hash)


def valid_passwd(passwd):
    for forbidden in forbidden_passwd.passwords:
        if passwd == forbidden:
            return False
        else:
            return True


def menu(items, back=True):
    if back:
        items.insert(0, "Back")
    for count, item in enumerate(items):
        print("[{}] {}".format(count, item))
    selection = menu_choose(len(items))
    return items[selection]


def menu_choose(length):
    print("Please select where to go.")
    while True:
        choice = get_int()
        if 0 <= choice < length:
            return choice
        else:
            print("You may only enter integers in the range of options.")
