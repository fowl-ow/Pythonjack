from Deck import Deck
from Card import Card
from Player import Player
from Dealer import Dealer
import Interactor


class Blackjack:
    deck = Deck()
    dealer = Dealer()
    menu = ["Settings", "Play"]

    def __init__(self):
        pass

    def login(self):
        print("""Hi, thanks for trying out my small program :D
        Please enter your username to log in, or enter 'create' to register a new account.
        You can quit *anytime* by typing 'exit'!
        """)
        str = input()
        Interactor.check_exit(str)


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