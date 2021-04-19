from Deck import Deck
from Hand import Hand
from Card import Card
from Interactor import *


class Player:
    name = ""
    passwd = ""
    hand = Hand()

    def __init__(self, create=True):
        if create:
            self.name = get_name()
            self.passwd = get_passwd()

    def change_name(self):
        self.name = get_name()

    def change_password(self):
        pass

    def draw(self, deck):
        self.hand.add_card(deck.draw())

    def clear_hand(self):
        self.hand.clear()
