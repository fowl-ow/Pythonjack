import re
from yes_no import yes, no


def get_name():
    while True:
        name = str.capitalize(get_input("Please enter your name:\n"))
        check_exit(name)
        if not (re.match('^\w+$', name) and 2 < len(name) < 13):
            print("Your name may only contain Alphanumeric characters,\nand must be between 3 and 12 characters long.")
        else:
            if get_decision("Are you happy with: {}?".format(name)):
                return name


def get_input(text):
    return check_exit(input(text))


def check_exit(str):
    if str.lower() == "exit":
        if get_decision("Are you sure?"):
            quit()
    return str

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
        check_exit(string)
        if not string.isdecimal():
            print("You may only enter integers.")
        else:
            return int(string)


def get_passwd():
    pass


def menu(items):
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
