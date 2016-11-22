"""
CS 335 - examples of Monte Carlo simulations to compute probabilities
"""

import random
import math
from random import shuffle

#===============================================
# Tic Tac Toe (a)
# 0 = X, 1 = O
#
#    0 | 1  | 2     
#    ---------
#    3 | 4 |  5  how board is represented with 
#    ----------     indices using a list
#    6 | 7  | 8
#

#===========================================================================
# TicTacToe(): a function that simulates a randomly played tic tac toe game
#              where X gets to choose first. Prints probablity of X winning
#===========================================================================

def TicTacToe():
    
    totalWins = 0               #keep track of total amount of times X wins
    for y in range(500):        #multiply trials run
        trials = 10000          #number of trials run
        numWins=0
        for t in range(trials):
            board = []                  #List representation of tic-tac-toe board
            xWins = 0                   #reset wins to 0 after each trial
            oWins = 0
            for x in range(9):              #during each loop an X or O is randomly chosen and 
                r = random.randrange(0,2)   #appended to spot on board assosciated with current loop #
                board.append(r)
                
            if (board[0] == board[1]) and (board[1] == board[2]):       #check the 8 ways you can win
                if board[0] == 0:
                    xWins = xWins + 1
                else:
                    oWins = oWins + 1
            if (board[3] == board[4]) and (board[4] == board[5]):       #3 in a row horizontally (3 ways)
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
            if (board[1] == board[4]) and (board[4] == board[7]):       #3 in a row vertically (3 ways)
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
            if (board[2] == board[4]) and (board[4] == board[6]):       #3 in a row diagonally (2 ways)
                if board[2] == 0:
                    xWins = xWins + 1
                else:
                    oWins = oWins + 1
            if (xWins > 0) and (oWins == 0):
                numWins = numWins + 1
                
        totalWins = totalWins + numWins             #keep track of wins
    print("Trial 1:")       
    print("probability X wins = ", totalWins/(trials*500))      #print probability that X wins




#===============================================
# Tic Tac Toe (b)
#=============================================================================
# checkWins(board): function that checks if X or O has a won after each turn.
#                   Returns winner (0 = X, 1 = O).
#=============================================================================

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
    choices = [0,1,2,3,4,5,6,7,8]           #list of 9 spots on board
    shuffle(choices)                            #randomize list order
    board = [-1,-1,-1,-1,-1,-1,-1,-1,-1]        #fill board with blanks until X or O is placed
    player = -1

    for turn in range(9):
        if turn%2 == 0:         # even loop number = playerX turn
            player = 0          
        else:
            player = 1          # odd = playerO turn
        board[choices[0]] = player      #randomly chosen location for placement of X or O
        if (checkWins(board) == 0) or (checkWins(board) == 1):
            winner = checkWins(board)       #check for winner
            return winner
        del choices[0]                      #remove board locations that have been used already
        shuffle(choices)                    #reshuffle available board locations
        
    return (-1)                     #return -1 (tie) if 9 turns have completed and no winner is found
def main():
    
    TicTacToe()
    
    totalXWins = 0
    totalOWins = 0                          #keep track of total winners and ties
    totalTies = 0
    for i in range(500):                    #multiply trials done
        xWins = 0
        oWins = 0                               #keep track of winners and ties
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

    print("Trial 2:")
    print("Probability X wins = ", totalXWins/(500000))
    print("Probability Y wins = ", totalOWins/(500000))     #print out probablity of X win, Y win and tie
    print("Probability Tie = ", totalTies/(500000))
    


main()




    
