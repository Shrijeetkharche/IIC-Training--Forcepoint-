class Cell:
    def __init__(self):
        self.mark = ""

    def isMarked(self) -> bool:
        return self.mark == 'X' or self.mark == 'O'