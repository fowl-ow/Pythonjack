

class Card:
    suit_list = {
        "Spades",
        "Hearts",
        "Clubs",
        "Diamonds"
    }

    rank_list = {
        "Ace": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "King": 10,
        "Queen": 10
    }

    suit = ""
    rank = ""
    value = 0

    def __init__(self, rank, suit):
        if rank not in self.rank_list or suit not in self.suit_list:
            print("CardInitError")
        else:
            self.rank = rank
            self.suit = suit
            self.value = self.rank_list[rank]

    def to_string(self):
        return str(self.rank + " of " + self.suit)