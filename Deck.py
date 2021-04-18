import random
from Card import Card


class Deck:

    deck = []
    card = Card("Ace", "Spades")

    def __init__(self):
         self.create()

    def create(self):
        for s in self.card.suit_list:
            for r in self.card.rank_list.keys():
                card = Card(r, s)
                self.deck.append(card)

    def shuffle(self):
        random.shuffle(self.deck)

    def clear(self):
        list.clear(self.deck)

    def draw(self):
        if len(self.deck) == 0:
            self.create()
        card = self.deck[0]
        self.deck.pop(0)
        return card