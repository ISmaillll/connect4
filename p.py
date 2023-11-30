# monticarlo AI resau de nuron
#web socet socket.io react flask
from copy import deepcopy
import csv
from math import inf
from random import random
from random import randint
import time

MAX = +1 
MIN = -1

class ConnectFourBoard :

    def __init__(self): 
        self.board = [['_' for _ in range(7)] for _ in range(6)]
        self.h = 0
        
    def utilFn(self,piece):
        if piece == MAX: return inf
        else: return -inf

    def heuristicEval(self,piece):
        pass

    def getPossibleMoves(self,piece):
        succs = list()
        for j in range(7):
            for i in range(6):
                if self.board[i][j]=='_':
                    successor = deepcopy(self)
                    successor.makeMove(i,j,piece)
                    break
            if i!=0:
                succs.append((i,j),successor)
        return succs
    
    def drawBoard(self):
        for i in range(6):
            line =" "
            for j in range(7):
                line += self.board[i][j]+"  "
            print(line)
        print()

    def makeMove(self,row,col,piece):
        if piece==MAX:
            self.board[row][col] = 'R'
        else:
            self.board[row][col] = 'Y'

    def win(self,piece):
        if piece==MAX: P = 'R'
        else: P = 'Y'
        #Diagonale Right
        for row in range(3, 6):
            for col in range(4):
                if all(self.board[row - i][col + i] == P for i in range(4)):
                    return True
        #Diagonale Left
        for row in range(3, 6):
            for col in range(3, 7):
                if all(self.board[row - i][col - i] == P for i in range(4)):
                    return True
        # Horisontale
        for row in range(6):
            if self.board[row][3] == P:
                for col in range(4):
                    if all(self.board[row][col+i] == P for i in range(4)):
                        return True
        # Verticale
        for col in range(7):
            if self.board[2][col] == P:
                for row in range(3):
                    if all(self.board[row+i][col] == P for i in range(4)):
                        return True
        return False
    
    @staticmethod
    def wtireWiner(piece):
        if piece==MAX:
            print("Red win")
        else:
            print("Yellow win")

    def gameOver(self):
        for j in range(7):
            if self.board[0][j] == '_':
                return False
        return True

    def moveInCol(self,col):
        find = False
        if col >=0 and col <=6:
            for i in range(5, -1, -1):
                if self.board[i][col]=='_':
                    find=True
                    break
            print(i)
            if find: return i
            else :return -1
        else : return -2  
          
class Play:

    def humanTurn() :
        pass
    
    def computerTurn() :
        pass

    @staticmethod
    def playrandom() :
        return randint(0, 6)
    
    @staticmethod
    def play(state,Turn):
        play_col=Play.playrandom()
        play_row=state.moveInCol(play_col)
        print(play_row,play_col)
        if play_row >=0:
            state.makeMove(play_row,play_col,Turn)
        return state
    def MinimaxAlphaBetaPruning():
        pass

def main():
    playing = True
    Turn = MAX
    state = ConnectFourBoard()
    state.drawBoard()

    while(playing):
        state = Play.play(state,Turn)
        state.drawBoard()
        time.sleep(0.4)
        if state.win(Turn):
            playing = False
            ConnectFourBoard.wtireWiner(Turn)
        elif state.gameOver():
            playing = False
            print("taie")
        Turn*=-1

if __name__ == "__main__":
    main()