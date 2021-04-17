from . import Card, Deck


class Blackjack:

    card = Card("Ace", "Spades")
    deck = Deck()

    deck.shuffle()
    for card in deck.deck:
        print(card.to_string())

    print("hi")

    deck.clear()
    for card in deck.deck:
        print(card.to_string())
