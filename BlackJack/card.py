class Card:
    cardValue = {'A': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
                '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        # return "{} of {}".format(self.value, self.suit)
        return f"{self.rank} of {self.suit}"

    def getCardValue(self):
        return Card.cardValue[self.rank]