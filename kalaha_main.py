# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:37:33 2022

@author: aksel
"""
from copy import deepcopy, copy

def showBoard (sides, goal_1, goal_2):
    ## Prints the state of the board
    print(" ","|",end=" ")

    for i in range(len(sides[0])):
        print(sides[0][i], end=" ")
    print("| ")
    
    print(goal_1,"|",end=" ")
    
    for i in range(len(sides[0])):
        print("-", end=" ")
    
    print("|",goal_2)
    
    print(" ","|",end=" ")
    for i in range(len(sides[1])):
        print(sides[1][i], end=" ")
    print("| "," \n")
    
def moveBalls (pick_place_p, sides_p, goal_1_p, goal_2_p, player_p):
    
    pick_place = copy(pick_place_p)
    sides = deepcopy(sides_p)
    goal_1 = copy(goal_1_p)
    goal_2 = copy(goal_2_p)
    player = copy(player_p)
    
    
    x = pick_place[0]
    y = pick_place[1]
    
    extra = 0
    
    
    #Player1 = sides[:][0]
    #print(Player1)
    
    hand = sides[x][y]
    
    #print("Hand", hand)
    
    
    if sum(sides[0][:]) != 0 and sum(sides[1][:]) != 0 : ##Check if the game is done
        sides[x][y]= 0
        while hand > 0: #Continue while some balls in the hand
            
            if player == 1: ## If player 1 is playing
                
                if x == 0:
                    y -=1
                elif x == 1:
                    y +=1
                #print("Test1", hand)
                #print("x, y",x,y,"", sides[x][y])
                if y <len(sides[0]) and x == 1: 
                ## Moves from left to right on the buttom board
                    
                    
                    sides[x][y]= sides[x][y]+1
                    hand = hand - 1
                    
                elif y == len(sides[0]) and x == 1:
                ##Skip goal 2 and change row and direction  
                    x = 0
                    y = y-1
                    sides[x][y]= sides[x][y]+1
                    hand = hand - 1
                
                elif y >= 0 and x == 0:
                ## Move from right to left  
                
                
                    sides[x][y]= sides[x][y]+1
                    hand = hand - 1
                    
                    if sides[x][y]-1 == 0 and hand == 0:
                        #print("Test")
                        goal_1 = goal_1 + 1 + sides[1][y]
                        sides[x][y] = 0
                        sides[1][y] = 0
                        
                elif y < 0 and x == 0:
                ## Add 1 ball to goal 1 when pasing the goal
                ## And change row and direction
                    x = 1
                    y = -1
                    
                    goal_1 += 1
                    
                    hand = hand - 1
                    if hand == 0: ##If the last ball is placed in goal, move again
                        #sides, goal_1, goal_2 = moveBalls([0,2], sides, goal_1, goal_2, player)
                        extra = 1
                    
            
            elif player == 2: #If player 2 is playing
                
                if x == 0:
                    y -=1
                elif x == 1:
                    y +=1
                
                if y <len(sides[0]) and x == 1:
                    
                    
                    sides[x][y]= sides[x][y]+1
                    hand = hand - 1
                    
                    if sides[x][y]-1 == 0 and hand == 0:
                        goal_2 = goal_2 + 1 + sides[0][y]
                        sides[x][y] = 0
                        sides[0][y] = 0
                    
                elif y == len(sides[1]) and x == 1:
                ## Add 1 ball to goal 2 when pasing the goal
                ## And change row and direction  
                    x = 0
                    
                    goal_2 += 1
                    
                    hand = hand - 1
                    if hand == 0: ##If the last ball is placed in goal, move again
                        #sides, goal_1, goal_2 = moveBalls([1,1], sides, goal_1, goal_2, player)
                        extra = 1
                
                elif y >= 0 and x == 0:
                ## Move from right to left  
                
                
                    sides[x][y]= sides[x][y]+1
                    hand = hand - 1
                
                elif y < 0 and x == 0:
                    
                    x = 1
                    y = -1
                    
                    
                    
                    hand = hand - 1    
            #print (hand)
    
        
    else:
        print("Game done")
        if goal_1 > goal_2:
            print("The winner is player 1", goal_1, " to ", goal_2)
        elif goal_1 < goal_2:
            print("The winner is player 2: ",goal_2, " to ", goal_1)
        else:
            print("It is a tie")
        
        print("Final board state")
        showBoard(sides, goal_1, goal_2)
    return sides, goal_1, goal_2, extra



def actions (sides_p,player_p):
    
    sides = deepcopy(sides_p)
    player = copy(player_p)
    
    a = []
    for i in range(0,6):
        if sides[player-1][i] != 0:
            a.append(i)
            
    return a

def result (pick_place, sides, goal_1, goal_2 ,player):
    
    sides_copy = deepcopy(sides)
    
    sides_new, goal_1_new, goal_2_new, extra = moveBalls(pick_place, sides_copy, goal_1, goal_2, player)

    return sides_new, goal_1_new, goal_2_new, extra



def utility (sides_p, goal_1_p, goal_2_p ,player_p):  
    
    sides = deepcopy(sides_p)
    goal_1 = copy(goal_1_p)
    goal_2 = copy(goal_2_p)
    player = copy(player_p)
    
    if player == 1:
        return copy(goal_1) - copy(goal_2)
    else:
        return copy(goal_2) - copy(goal_1)
    
def terminal (sides_p):  
    
    sides = deepcopy(sides_p)
    
    if sum(sides[0][:]) != 0 and sum(sides[1][:]) != 0 : ##Check if the game is done
        return False 
    else:
        return True



def maxNode (sides_p, goal_1_p, goal_2_p ,player_p,depth):
    
    
    
    sides = deepcopy(sides_p)
    goal_1 = copy(goal_1_p)
    goal_2 = copy(goal_2_p)
    player = copy(player_p)
    
    move = -10
    
    #print("maxNode")
    #print("depth")
    #print(depth)
    #showBoard(sides, goal_1, goal_2)
    
    if (player == 1):
        opponent = 2
    else:
        opponent = 1
    
    if depth > 3 or terminal(sides):
        return utility(sides, goal_1, goal_2 ,player),move
    v = float('-inf')
    
    a = actions(sides,player)
    #print(a)
    for i in a:
        sides_n, goal_1_n, goal_2_n, extra = result([player-1,i], sides, goal_1, goal_2 ,player)
        if (extra == 0):
            
            value , m = minNode(sides_n, goal_1_n, goal_2_n ,opponent,depth+1)
        elif (extra == 1):
            value , m = maxNode(sides_n, goal_1_n, goal_2_n ,player,depth)
            
        
        
        if (value > v):
            v = copy(value)
            move = copy(i)
    
    return v , move
    
            
    
def minNode (sides_p, goal_1_p, goal_2_p ,player_p,depth):
    
    
    
    sides = deepcopy(sides_p)
    goal_1 = copy(goal_1_p)
    goal_2 = copy(goal_2_p)
    player = copy(player_p)
    
    move = -10
    
    #print("minNode")
    #print("depth")
    #print(depth)
    #showBoard(sides, goal_1, goal_2)
    
    if (player == 1):
        opponent = 2
    else:
        opponent = 1
    
    if depth > 3 or terminal(sides):
        return utility(sides, goal_1, goal_2 ,player), move
    v = float('inf')
    
    a = actions(sides,player)
    #print(a)
    for i in a:
        sides_n, goal_1_n, goal_2_n, extra = result([player-1,i], sides, goal_1, goal_2 ,player)
        if (extra == 0):
            value,m = maxNode(sides_n, goal_1_n, goal_2_n ,opponent,depth+1)
        elif (extra == 1):
            value,m = minNode(sides_n, goal_1_n, goal_2_n ,player,depth)
        
        if (value < v):
            v = copy(value)
            move = copy(i)
    return v,move



# Defining main function
def main():
    sides = [[4,4,4,4,4,4],[4,4,4,4,4,4]]
    goal_1 = 0
    goal_2 = 0
    
    print("Initial board state")
    showBoard(sides, goal_1, goal_2)
    
    #value,move = maxNode(sides, goal_1, goal_2, 1, 0)
    #print(value)
    
    finished = 0
    player_turn = 1
    
    while finished == 0:
        
        if player_turn == 1:
            
            player_move = int(input("what bowl do you want to move?"))
            sides, goal_1, goal_2,extra  = moveBalls([1,player_move], sides, goal_1, goal_2, 2)
            showBoard(sides, goal_1, goal_2)
            if extra == 0:
                player_turn = 0
        else:
            
            print("robot turn")
            value,move = maxNode(sides, goal_1, goal_2, 1, 0)
            
            
            sides, goal_1, goal_2,extra = moveBalls([0,move], sides, goal_1, goal_2, 1)
            showBoard(sides, goal_1, goal_2)
            if extra == 0:
                player_turn = 1
                
            
        if terminal(sides) == 1:
            finished = 1
            
            
            
    print("Final board state")
    showBoard(sides, goal_1, goal_2)
  
    
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()
      

## Initilize the values of the board
#sides = [[6,6,6,6,6,6],[6,6,6,6,6,6]]
#sides = [[1,6,6,6,6,8],[9,6,6,6,6,8]]
#sides = [[0,0,0,0,0,0],[2,6,6,6,6,6]] ## Test if Game ends correctly
#sides = [[2,6,6,6,6,6], [0,0,0,0,0,0]] ## Test if Game ends correctly
#sides = [[2,13,6,6,6,6], [6,6,6,6,6,13]] ## Test state for adding the opponenets balls, 
                                         ##when hidding your own empty bowl
#sides = [[1,5,2,4,3,1],[0,5,3,4,1,1]] ##For testing moving with last ball ending in goal, and repicking                                      
#sides, goal_1, goal_2 = moveBalls([0,0], sides, goal_1, goal_2, 1)
#print("Move 1")
#showBoard(sides, goal_1, goal_2)

#sides, goal_1, goal_2 = moveBalls([1,5], sides, goal_1, goal_2, 2)
#print("Move 2")
#showBoard(sides, goal_1, goal_2)                                        

#goal_1 = 1
#goal_2 = 2


#print("Initial board state")
#showBoard(sides, goal_1, goal_2)

#s = sides
#g1 = goal_1
#g2 = goal_2

#sides, goal_1, goal_2 = moveBalls([0,0], sides, goal_1, goal_2, 1)
#print("Move 1")
#showBoard(sides, goal_1, goal_2)

#sides, goal_1, goal_2 = moveBalls([1,5], sides, goal_1, goal_2, 2)
#print("Move 2")
#showBoard(sides, goal_1, goal_2)