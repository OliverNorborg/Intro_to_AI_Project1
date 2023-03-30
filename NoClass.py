# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:06:21 2022

@author: s174030
"""


#balls = 6
"""Initializing bord game"""
state = {0: [6,6,6,6,6,6,0], 1: [6,6,6,6,6,6,0]}
playersturn = 0
if playersturn == 1:
    opponentsturn = 0
else:
    opponentsturn = 1


        
def printboard():
    #creating a revered array of opponent since it is anti clock wise
    reversed_opppont = state[opponentsturn][0:-1].reverse()
    print("Bowls:             1  2  3  4  5  6 ")
    print("Opponents bowls: ", state[opponentsturn][0:-1])
    print("Goals          ",state[opponentsturn][-1:], "              ", state[playersturn][-1:])
    print("Players bowls:   ", state[playersturn][0:-1])
    
def choose_bowl(bowl):
    bowl = bowl-1
        
    if bowl > 5:
        print("Illegal move")
        return False
        
    if bowl < 0:
        print("Illegal move")
        return False
        
    """if self.playersturn == 1:
        opponentsturn = 0
    else:
        opponentsturn = 1"""
            
    # Uncomment the 2 lines below to show what it looks like before the action
    print("The current board look like:")
    print(state)
    printboard()
    
    #We make a list contining only either players or the opponents 'opptions'
    #We only keep the goal of the current player since the player can't 
    #place anything in the other goal 
    #This also ordres the side of the current player
    board_state = state[playersturn] + state[opponentsturn]
    board_state = board_state[0:-1]

    #Find how mny balls are in one of the bowls and assign it to balls variable 
    #Set the bowls value to 0 since we took all the balls.  
    balls = board_state[bowl]
    board_state[bowl] = 0
    
    #Updating the board when a bowl has been choosen. 
    for _ in range(balls):
        bowl += 1
        if bowl >= len(board_state):
            bowl = 0
        board_state[bowl] += 1
        
    #Updating the state with the new board state. 
    state[playersturn] = board_state[0:7]
    state[opponentsturn]=board_state[7:13] + [state[opponentsturn][-1]]
    print(state)
    #Uncomment the 2 below to see the board after the action
    print("The new state is")
    printboard() 
    
    



""" Test section """


printboard()
choose_bowl(4)
choose_bowl(5)








