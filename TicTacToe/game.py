from board import Board
from player import Player

game1 = None

class Game:
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name, 'X')
        self.player2 = Player(player2Name, 'O')
        self.board = Board()
        self.gameEnd = False
        self.turn = 0

    @staticmethod
    def createGame(player1Name, player2Name):
        global game1
        if game1 != None:
            return game1
        game1 = Game(player1Name, player2Name)
        return game1

    def getGameStatus(self):
        self.board.printBoard()

    def play(self, index):
        self.getGameStatus()
        if self.board.allMarked() or self.gameEnd:
            print("Game is already concluded!")
            return True

        if self.board.isCellMarked(index):
            print(f"Cell {index} is already Marked!")
            return 
        i, j = int(index[0]), int(index[1])
        if self.turn == 0:
            # Player 1 Turn
            # self.player1.markCell(self.board.cells[i][j])
            self.board.cells[i][j].mark = self.player1.symbol
            flag, description = self.board.resultAnalyzer()
            if flag:
                self.gameEnd = True
                print(f'{self.player1.name} Wins!')
                print(description)
                return True
            self.turn = 1
        elif self.turn == 1:
            # Player 2 Turn
            # self.player2.markCell(self.board.cells[i][j])
            self.board.cells[i][j].mark = self.player2.symbol
            flag, description = self.board.resultAnalyzer()
            if flag:
                self.gameEnd = True
                print(f'{self.player2} Wins!')
                print(description)
                return True
            self.turn = 0

                
if __name__ == "__main__":
    G = Game.createGame('Shri', 'Jeet')
    G2 = Game.createGame('A', 'B')

    print(G2.player1.name)

    # G.getGameStatus()

    # G.play('22')
    # G.getGameStatus()
