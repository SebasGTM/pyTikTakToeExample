from time import sleep
import random

from numpy import size, true_divide


class TikTakToe:

    def __init__(self, player1, player2):
        self.Board = [" " for x in range(9)]
        self.ActivePlayer = None
        self.TurnNo = 1
        self.Player1 = player1
        self.Player2 = player2
        self.Sym_Free = " "

    def drawBoard(self):
        line = "\n" + "".join(["|"+val if idx % 3 != 0 or idx == 0 else "|\n|"+val for idx, val in enumerate(self.Board)]) + "|\n"
        print(line)

    
    def start(self):
        
        self.Player1.Name = "Player 1 ({0})".format(self.Player1.Symbol)
        self.Player2.Name = "Player 2 ({0})".format(self.Player2.Symbol)
        self.ActivePlayer = self.Player1
        self.play()


    def play(self):

        while True:
            self.drawBoard()
            choice = self.ActivePlayer.makeMove(self.Board)

            self.TurnNo+=1
            if self.TurnNo > 5:
                if self.checkWinner(choice):
                    print("Game Ended. Winner: " + self.ActivePlayer.Name)
                    break
                elif [idx for idx, val in enumerate(self.Board) if val == " "].size == 0:
                    print("Game Ended. Tie")
                    break

            if self.ActivePlayer == self.Player1:
                self.ActivePlayer = self.Player2
            else:
                self.ActivePlayer = self.Player1       
                
        

    def checkWinner(self, square):
        sym = self.Board[square]
        rowlen = 3
        colLen = 3
        rowIdx = square // rowlen
        row = self.Board[rowIdx * rowlen : (rowIdx+1) * rowlen]
        if all([s == sym for s in row]):
            return True

        colIdx = square % rowlen
        col = [self.Board[colIdx + (x*colLen)] for x in range(colLen)]
        if all([s == sym for s in col]):
            return True

        # dialgonal check only for 0, 2, 4, 6, 8
        if square % 2 == 0:
            diagX = [self.Board[i] for i in [0, 4, 8]]
            if all([s == sym for s in diagX]):
                return True

            diagY = [self.Board[i] for i in [2, 4, 6]]
            if all([s == sym for s in diagY]):
                return True

        return False



    @staticmethod
    def createHumanPlayer(symbol):
        return TikTakToe.HumanPlayer(symbol)

    @staticmethod
    def createCpuPlayer(symbol):
        return TikTakToe.CpuPlayerRandom(symbol)

    
    class HumanPlayer:

        def __init__(self, symbol):
            self.Symbol = symbol

        def makeMove(self, board):
            sel = input("Your Turn. Enter your choise as a number (1-9): ")
            while not self.isValid(sel, board):
                sel = input("Wrong input! Enter your choise as a number (1-9): ")

            idx = int(sel)-1
            board[idx] = self.Symbol

            return idx

        def isValid(self, val, board):
            if val.isdigit():
                sel = int(val)
                if sel > 0 and sel < 10:
                    if board[sel-1] == " ":
                        return True

            return False


    class CpuPlayerRandom:
        
        def __init__(self, symbol):
            self.Symbol = symbol
            self.Difficulty = 1

        def makeMove(self, board):
            print("Computers turn. . . ")
            sleep(.7)
            freeList = [idx for idx, val in enumerate(board) if val == " "]
            idx = random.choice(freeList)
            board[idx] = self.Symbol

            return idx

if __name__ == '__main__':
    game = TikTakToe(TikTakToe.createHumanPlayer("X"), TikTakToe.createCpuPlayer("O"))
    game.start()