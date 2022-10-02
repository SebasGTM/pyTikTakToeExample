from time import sleep


class TikTakToe:

    def __init__(self):
        self.Board = [" " for x in range(9)]
        self.GameResult = None
        self.NextTurn = "H"
        self.Difficulty = 1
        self.TurnNo = 0
        self.Sym_X = "X"
        self.Sym_O = "O"
        self.Sym_Free = " "

    def drawBoard(self):
        line = "\n" + "".join(["|"+val if idx % 3 != 0 or idx == 0 else "|\n|"+val for idx, val in enumerate(self.Board)]) + "|\n"
        print(line)

    
    def start(self):
        
        sel = ""
        while not sel == "H" or sel == "C" :
            sel = input("Who will start (H = Human, C = Computer): ")

        self.PlayerTurn = sel
        self.play()

              
    def play(self):

        while True:
            self.drawBoard()
            if self.NextTurn == "H":
                sqare = self.playerTurn()
                self.NextTurn = "C"
            else:
                sqare = self.cpuTurn()
                self.NextTurn = "H"

            self.TurnNo+1
            if self.TurnNo > 5:
                self.checkGamestate(sqare)

        


    def checkGamestate(self, sqare):
        checked = [idx for idx, val in enumerate(self.Board) if val != self.Sym_Free]



    def cpuTurn(self):        
        print("Computers turn. . . ")
        sleep(.7)
        idx = next(idx for idx, val in enumerate(self.Board) if val != self.Sym_Free)
        self.Board[idx] = self.Sym_O
        
        return idx



    def playerTurn(self):
        sel = ""
        while not self.isValid(sel):
            sel = input("Your Turn. Enter your choise as a number (1-9): ")

        idx = int(sel)-1
        self.Board[idx] = self.Sym_X

        return idx



    def isValid(self, val):
        sel =0
        if val.isdigit():
            sel = int(val)
            if sel > 0 and sel < 10:
                if self.isEmptyField(self.Board[sel-1]):
                    return True

        return False

    def isEmptyField(self,val):
        if val == self.Sym_Free:
            return True
        else:
            return False
        

game = TikTakToe()
game.start()