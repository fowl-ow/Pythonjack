from . import Card, Deck


class Hand:
    hand = []
    value = 0

    def __init__(self):
        pass

    def update_value(self):
        ace = False
        self.value = 0
        if len(self.hand) == 0:
            return
        for card in self.hand:
            self.value += card.value
            if card.rank == "Ace": ace = True
        if self.value >= 11: self.value += 10

    def add_card(self, card):
        self.hand.append(card)
        self.update_value()

    def clear(self):
        list.clear(self.deck)
