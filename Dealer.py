from Hand import Hand


class Dealer:
    hand = Hand()

    def __init__(self):
        pass

    def draw(self, deck):
        self.hand.add_card(deck.draw())

    def clear_hand(self):
        self.hand.clear()
