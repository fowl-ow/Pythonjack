import re
from yes_no import yes, no


def get_name():
    while True:
        name = str.capitalize(input("Please enter your name:\n"))
        if not (re.match('^\w+$', name) and len(name) > 2 and len(name) < 13):
            print("Your name may only contain Alphanumeric characters,\nand must be between 3 and 12 characters long.")
        else:
            if get_bool("Are you happy with: {}?".format(name)):
                return name


def get_bool(text):
    while True:
        temp = str.lower(input(text + "\n"))
        for synonym in yes:
            if temp == synonym: return True
        for synonym in no:
            if temp == synonym: return False
        print("Sorry I didn't catch that.")


def get_passwd():
    pass

def menu():
    pass
