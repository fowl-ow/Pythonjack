import json
import re
from yes_no import yes, no
from getpass import getpass
from passlib.hash import bcrypt


class Interactor:

    def get_name(self):
        while True:
            name = str.capitalize(self.get_input("Please enter your name:\n"))
            self.check_exit(name)
            if not (re.match('^\w+$', name) and 2 < len(name) < 13):
                print(
                    "Your name may only contain Alphanumeric characters,\nand must be between 3 and 12 characters long.")
            else:
                if self.get_decision("Are you happy with: {}?".format(name)):
                    return name

    def get_input(self, text):
        return self.check_exit(input(text))

    def check_exit(self, str):
        if str.lower() == "exit":
            if self.get_decision("Are you sure?"):
                quit()
        return str

    def get_decision(self, text):
        while True:
            temp = str.lower(self.get_input(text + "\n"))
            self.check_exit(temp)
            for synonym in yes:
                if temp == synonym: return True
            for synonym in no:
                if temp == synonym: return False
            print("Sorry I didn't catch that.")

    def get_int(self):
        while True:
            string = self.get_input()
            self.check_exit(string)
            if not string.isdecimal():
                print("You may only enter integers.")
            else:
                return int(string)

    def set_passwd(self, username):
        for i in range(9):
            print("Please enter a strong password.")
            hash = bcrypt.hash((getpass()))
            print("Please confirm your password.")
            if print(bcrypt.verify(getpass(), hash)):
                with open("data.json", "w") as writefile:
                    json.dump(dictionary, writefile)

            else:
                print("Mismatch.")
        print("Failed 9 times, I give up.")
        quit()

    def verify_passwd(self, username):
        pass

    def menu(self, items):
        items.insert(0, "Back")
        for count, item in enumerate(items):
            print("[{}] {}".format(count, item))
        selection = self.menu_choose(len(items))
        return items[selection]

    def menu_choose(self, length):
        print("Please select where to go.")
        while True:
            choice = self.get_int()
            if 0 <= choice < length:
                return choice
            else:
                print("You may only enter integers in the range of options.")

    def sefes(self):
        with open("data.json", "r+") as f:
            dictionaries = json.load(f)
            for dic in dictionaries:
                print(dic.get("uid"))
            f.seek(0)
            json.dump(dictionaries, f, indent=4)
