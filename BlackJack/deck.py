import random
from card import Card

class Deck:
    def __init__(self, cards):
        self.cards = cards
        self.totaldrawnCards = []

    @staticmethod
    def createDeck():
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cards = [Card(suit, rank) for suit in suits for rank in ranks]
        return Deck(cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        card = random.choice(self.cards)
        self.cards.remove(card)
        self.totaldrawnCards.append(card)
        return card

