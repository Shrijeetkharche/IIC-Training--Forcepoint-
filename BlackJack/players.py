class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.drawnCards = []
        self.points = 0
        self.choice = ''
        self.result = ''

    def drawCard(self, deck):
        card = deck._deal()
        self.drawnCards.append(card)
        if card.rank == 'A':
            points = 1 if 11 + self.points > 21 else 11
            self.points += points
            self.printDraw(card, points)
            return True
        points = card.getCardValue()
        self.points += points
        self.printDraw(card, points)
        return True

    def printDraw(self, card, points):
        print(f'\t Player Name: {self.playerName}')
        print(f"\t Card Drawn: {card}, Card Points: {points}")
        print(f"\t Total Points: {self.points}")
    