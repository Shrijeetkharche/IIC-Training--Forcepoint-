from card import Card
from deck import Deck
from players import Player


class Game:
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        self.deck = Deck.createDeck()
        self.gameEnd = False
        self.turn = 0

    def getGameStatus(self):
        print('-'*20)
        print(f'PLayer 1: {self.player1.playerName}')
        print(f'Drawn Cards: {self.player1.drawnCards}, Total Points: {self.player1.points}')
        print(f'PLayer 2: {self.player2.playerName}')
        print(f'Drawn Cards: {self.player2.drawnCards}, Total Points: {self.player2.points}')
        print('-'*20)
        if self.gameEnd:
            print('\n')
            print(f'Player 1: {self.player1.result}, Player 2: {self.player2.result}')
            print('\n')
        print('-'*20)

    def checkPassRule(self, decision):
        if self.turn == 0:
            print('Player 1 called PASS')
            if self.player1.choice == decision:
            # Checks for the consecutive PASS from the player 1.
                self.gameEnd = True
                self.player1.result = 'Lose'
                self.player2.result = 'Win'
                print(f'{self.player2.playerName} Wins!')
            self.player1.choice = decision.lower()
            self.turn = 1
        elif self.turn == 1:
            print('Player 2 called PASS')
            if self.player2.choice == decision:
            # Checks for the consecutive PASS from the player 2.
                self.gameEnd = True
                self.player1.result = 'Win'
                self.player2.result = 'Lose'
                print(f'{self.player1.playerName} Wins!')
            self.player2.choice = decision.lower()
            self.turn = 0

    def resultAnalyser(self):
        if self.player1.points == 21:
            description = "Player 1 Wins, Player 2 Lose."
            self.gameEnd = True
            return True, description
        if self.player2.points == 21:
            description = "Player 2 Wins, Player 1 Lose."
            self.gameEnd = True
            return False, description

        if self.player1.points > 21:
            description = "Player 2 Wins, Player 1 Lose."
            self.gameEnd = True
            return False, description
        if self.player2.points > 21:
            description = "Player 1 Wins, Player 2 Lose."
            self.gameEnd = True
            return True, description
        return None, None

    def play(self, decision = 'Deal'):
        # 
        self.getGameStatus()
        if self.gameEnd:
            print('Game is already concluded.')
            return

        if decision.lower() == "pass":
            self.checkPassRule(decision)
            return

        if self.turn == 0:
            # Player 1 Turn
            self.player1.choice = decision.lower()
            _ = self.player1.drawCard(self.deck)
            self.turn = 1
            flag, description = self.resultAnalyser()
            if flag:
                self.gameEnd = True
                self.player1.result = 'Win'
                self.player2.result = 'Lose'
                print(f'{self.player1.playerName} Wins!')
                print(description)
                return True
        elif self.turn == 1:
            # Player 2 Turn
            self.player2.choice = decision.lower()
            _ = self.player2.drawCard(self.deck)
            self.turn = 0
            flag, description = self.resultAnalyser()
            if flag is False:
                self.gameEnd = True
                self.player1.result = 'Lose'
                self.player2.result = 'Win'
                print(f'{self.player2.playerName} Wins!')
                print(description)
                return True


if __name__ == "__main__":
    G = Game('Shri', 'Jeet')

    G.play('pass')
    G.play()

    G.play('pass')

    G.getGameStatus()



        