from Deck import Deck
from Hand import Hand
from Card import Card
import Interactor

class Player:
    name = ""
    passwd = ""
    hand = Hand()

    def __init__(self, name, passwd, create=True):
        if create:
            self.name = name
            self.passwd = passwd

    def set_password(self):
        Interactor.set_password(self.name)

    def draw(self, deck):
        self.hand.add_card(deck.draw())

    def clear_hand(self):
        self.hand.clear()
