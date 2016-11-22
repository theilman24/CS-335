"""
CS 335 - examples of Monte Carlo simulations to compute probabilities
"""

import random
import math
from random import shuffle
"""

# Tic Tac Toe (a)
# 0 = X, 1 = O
totalWins = 0
for y in range(500):
    trials = 10000
    numWins=0
    for t in range(trials):
        board = []
        xWins = 0
        oWins = 0
        for x in range(9):
            r = random.randrange(0,2)
            board.append(r)
            

        if (board[0] == board[1]) and (board[1] == board[2]):
            if board[0] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (board[3] == board[4]) and (board[4] == board[5]):
            if board[3] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (board[6] == board[7]) and (board[7] == board[8]):
            if board[6] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (board[0] == board[3]) and (board[3] == board[6]):
            if board[0] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (board[1] == board[4]) and (board[4] == board[7]):
            if board[1] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (board[2] == board[5]) and (board[5] == board[8]):
            if board[2] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (board[0] == board[4]) and (board[4] == board[8]):
            if board[0] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (board[2] == board[4]) and (board[4] == board[6]):
            if board[2] == 0:
                xWins = xWins + 1
            else:
                oWins = oWins + 1
        if (xWins > 0) and (oWins == 0):
            numWins = numWins + 1
            
    totalWins = totalWins + numWins
    ##print(numWins/trials)
print(totalWins/(trials*500))

"""
def checkWins(board):
    if (board[0] == board[1]) and (board[1] == board[2]) and (board[0] != -1):
            return board[0]
    if (board[3] == board[4]) and (board[4] == board[5]) and (board[3] != -1):
            return board[3]
    if (board[6] == board[7]) and (board[7] == board[8]) and (board[6] != -1):
            return board[6]
    if (board[0] == board[3]) and (board[3] == board[6]) and (board[0] != -1):
            return board[0]
    if (board[1] == board[4]) and (board[4] == board[7]) and (board[1] != -1):
            return board[1]
    if (board[2] == board[5]) and (board[5] == board[8]) and (board[2] != -1):
            return board[2]
    if (board[0] == board[4]) and (board[4] == board[8]) and (board[0] != -1):
            return board[0]
    if (board[2] == board[4]) and (board[4] == board[6]) and (board[2] != -1):
            return board[2]
    



def Game():
    # 0 = Xplayer and 1 = Oplayer
    choices = [0,1,2,3,4,5,6,7,8]
    shuffle(choices)
    board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    player = -1

    for turn in range(9):
        if turn%2 == 0:
            player = 0
        else:
            player = 1
        board[choices[0]] = player
        if (checkWins(board) == 0) or (checkWins(board) == 1):
            winner = checkWins(board)
            return winner
        del choices[0]
        shuffle(choices)
        
    return (-1)       
def main():
    
    totalXWins = 0
    totalOWins = 0
    totalTies = 0
    for i in range(500):
        xWins = 0
        oWins = 0
        tie = 0
        for x in range(1000):
            theWinner = Game()
            if(theWinner == 0):
                xWins = xWins + 1
            if(theWinner == 1):
                oWins = oWins + 1
            if(theWinner == -1):
                tie = tie + 1
        totalXWins = totalXWins + xWins
        totalOWins = totalOWins + oWins
        totalTies = totalTies + tie

    print("total X wins", totalXWins/(500000))
    print("total Y wins", totalOWins/(500000))
    print("total Ties", totalTies/(500000))
    


main()




    
