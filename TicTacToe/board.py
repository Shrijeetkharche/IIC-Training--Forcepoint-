from cell import Cell

class Board:
    def __init__(self):
        self.cells = [[Cell() for _ in range(3)] for _ in range(3)]

    @staticmethod
    def check(case):
        if "".join(case) == "XXX":
            return True, "Player1 Win, Player2 Lose"
        elif "".join(case) == "OOO":
            return True, "Player2 Win, Player1 Lose"
        else:
            return None, None

    def isCellMarked(self, index):
        i, j = int(index[0]), int(index[1])
        if self.cells[i][j]:
            return False
        return True

    def allMarked(self):
        for lst in self.cells:
            for i in lst:
                if i.mark == "":
                    return False
        return True

    def printBoard(self):
        for lst in self.cells:
            line = []
            for j in lst:
                if j.mark:
                    line.append(j.mark)
                else:
                    line.append('_')
            print(" ".join(line))

    def resultAnalyzer(self):
        # Horizontal Cases:
        for i in range(3):
            case = []
            for j in range(3):
                case.append(self.cells[i][j].mark)
            flag, description = Board.check(case)
            if flag:
                return flag, description
            
        # Vertical Cases:
        for i in range(3):
            case = []
            for j in range(3):
                case.append(self.cells[j][i].mark)
            flag, description = Board.check(case)
            if flag:
                return flag, description
            
        # Diagonal Cases:
        diagCase1 = [self.cells[i][i].mark for i in range(3)]
        flag, description = Board.check(diagCase1)
        if flag:
            return flag, description
        
        diagCase2 = [self.cells[i][2-i].mark for i in range(3)]
        flag, description = Board.check(diagCase2)
        if flag:
            return flag, description

        if not self.allMarked():
            print('Game not concluded yet.')
            return None, None
        else:
            return False, "Draw"





# if __name__ == "__main__":
#     b = Board()

# 00 01 02
# X  X  X
# 10 11 12
# X  O  X
# 20 21 22
# O  X  O