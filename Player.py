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

    def