from Deck import Deck
from Card import Card
from Player import Player
from Dealer import Dealer
import Interactor as intr
from Database import Database
from forbidden_names import names
import getpass

class Blackjack:
    deck = Deck()
    dealer = Dealer()
    db = Database()

    def __init__(self):
        pass

    def login_menu(self):
        print("Hi, thanks for trying out my small program :D")
        print("You can quit *anytime* by typing 'quit'!")
        while True:
            print("What would you like to do:")
            choice = intr.menu(["Login", "Create Account", "Quit"], back=False)
            if choice == "Login":
                self.login()
            if choice == "Create Account":
                self.create_account()
            if choice == "Quit":
                intr.check_exit("quit")

    def login(self):
        for i in range(3):
            name = intr.get_name("Please enter your username:\n", login=True)
            passwd = intr.get_passwd()
            if self.db.user_exists(name) and intr.password_verified(name, passwd):
                self.main_menu()
            else:
                print("Username or password wrong.")

    def create_account(self):
        for i in range(3):
            name = intr.get_name("Please enter a name:\n")
            if not self.db.user_exists(name):
                passwd = intr.set_passwd()
                self.db.create_user(name)
                self.db.set_passwd(name, passwd)
                "Account created!"
                return
            print("Name already taken.")
        print("Returned to login due to 3 failed tries.")

    def settings_menu(self):
        pass

    def main_menu(self):
        print("nice")
