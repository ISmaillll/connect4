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

    def __init__(self,depth=0,piece=MAX): 
        self.board = [['_' for _ in range(7)] for _ in range(6)]
        self.piece = piece
        self.depth = depth
        self.Action = (0,0)
        self.NextAction = (0,0)
        self.value = 0
        self.alpha = 0
        self.beta = 0
        
    def Win_Value(self,piece):
        if piece == MAX: return inf
        else: return -inf

    def heuristicEval(self,piece):
        if piece == MAX: return 10
        else: return -10

    def getPossibleMoves(self,piece):
        succs = list()
        for j in range(7):
            find = False
            for i in range(5, 0, -1):
                if self.board[i][j]=='_':
                    find=True
                    successor = deepcopy(self)
                    successor.depth = self.depth+1
                    successor.piece = self.piece*-1
                    successor.Action = (i,j)
                    successor.makeMove(i,j,piece)
                    break
            if find:
                succs.append(successor)
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

    def Tie(self):
        for j in range(7):
            if self.board[0][j] == '_':
                return False
        return True

    def gameOver(self,piece):
        return self.Tie() or self.win(piece)

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
    @staticmethod
    def computerTurn(state) :
        NextAction , NextValue = Play.minimaxAlphaBetaPruning(state,2,-inf,+inf,MAX)
        return NextAction

    @staticmethod
    def playrandom(state) :
        play_row = -1
        while play_row == -1:
            play_col=randint(0, 6)
            play_row=state.moveInCol(play_col)
        
        return play_col , play_row
    
    @staticmethod
    def play(state,Turn):
        if Turn == MAX:
            print("AI")
            play_col , play_row = Play.computerTurn(state)
        else :
            print("Random")
            play_col , play_row = Play.playrandom(state)
        print(play_row,play_col)

        return play_col , play_row
    @staticmethod
    def minimaxAlphaBetaPruning(state, depthlim, alpha=-inf, beta=+inf, piece=MAX):
        if state.depth < depthlim or not state.gameOver(state.piece):
            if piece==MAX:
                state.value = -inf
                state.alpha = -inf
                state.beta = +inf
                for successor in state.getPossibleMoves(piece):
                    NextAction , NextValue = Play.minimaxAlphaBetaPruning(successor,depthlim,state.alpha,state.beta,MIN)
                    state.value = max(state.value,NextValue)
                    state.alpha = max(state.value,alpha)
                    if state.value == NextValue:state.NextAction = NextAction
                    if state.value >=beta:
                        return state.Action,state.value 
            else:
                state.value = inf
                state.alpha = -inf
                state.beta = inf
                for successor in state.getPossibleMoves(piece):
                    NextAction , NextValue = Play.minimaxAlphaBetaPruning(successor,depthlim,state.alpha,state.beta,MAX)
                    state.value = min(state.value,NextValue)
                    state.beta = min(state.value,beta)
                    if state.value == NextValue:state.NextAction = NextAction
                    if state.value <=alpha:
                        return state.Action,state.value
        if state.gameOver(state.piece):
            if state.Tie():
                state.value = 0
            else:
                state.value = state.Win_Value(state.piece)
        else :
            state.value = state.heuristicEval(state.piece)
        return state.Action,state.value    

def main():
    playing = True
    Turn = MAX
    state = ConnectFourBoard()
    state.drawBoard()

    while(playing):
        #
        play_col , play_row = Play.play(state,Turn)
        state.makeMove(play_row,play_col,Turn)
        state.drawBoard()
        time.sleep(0.4)
        # end game 
        if state.gameOver(Turn):
            if state.Tie():
                print("tie")
            else :
                ConnectFourBoard.wtireWiner(Turn)
            playing = False
            
        # change player
        Turn*=-1

if __name__ == "__main__":
    main()