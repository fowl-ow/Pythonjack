from Deck import Deck
from Card import Card
from Player import Player
from Dealer import Dealer
from Interactor import Interactor
from Database import Database
from forbidden import names


class Blackjack:
    deck = Deck()
    dealer = Dealer()
    inter = Interactor()
    menu = ["Settings", "Play"]
    db = Database()

    def __init__(self):
        pass

    def login_menu(self):
        print("Hi, thanks for trying out my small program :D")
        print("You can quit *anytime* by typing 'exit'!")
        while True:
            print("What would you like to do:")
            choice = self.inter.menu(["Login", "Create Account", "Exit"], back=False)
            if choice == "Login":
                self.login()
            if choice == "Create Account":
                self.create_user()
            if choice == "Exit":
                self.inter.check_exit("exit")

    def login(self):
        for i in range(3)
            name = self.inter.get_name(just_check=True)
            if not self.db.create_user(True)


    def create_user(self):
        for i in range(3):
            name = self.inter.get_name()
            for forbidden in names:
                if name.lower() == forbidden:
                    print("Name forbidden.")
            if self.db.create_user(name):
                passwd = self.inter.get_passwd(self)
                self.db.set_passwd(name, passwd)
                "Account created!"
                return
            print("Name already taken.")
        print("Returned to login due to 3 failed tries.")

    def main_menu(self):
        while True:
            choice = Interactor.menu(["One", "Two", "Three"])
            if choice == "One":
                pass
            if choice == "Two":
                pass
            if choice == "Three":
                pass

    def settings_menu(self):
        while True:
            choice = Interactor.menu("Test")

    def game_menu(self):
        pass