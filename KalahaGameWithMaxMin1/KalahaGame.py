# -*- coding: utf-8 -*-
"""
Kalaha Game for Intorduction to Ai, 02180

Group 25
"""
#import copy 


class Game:
    def __init__(self):
        self.balls = 6
        self.state = {0: [6,6,6,6,6,6,0], 1: [6,6,6,6,6,6,0]}
        self.playersturn = 0

        
    def get_state(self):
        return copy.deepcopy(self.state)
    
    def turn(self) :
        return self.playersturn
        
    
    def choose_bowl(self, bowl):
        bowl = bowl-1
        
        if bowl > 5:
            print("Illegal move")
            return False
        if bowl < 0:
            print("Illegal move")
            return False
        if self.playersturn == 1:
            opponentsturn = 0
        else:
            opponentsturn = 1
            
        #print("Playerturn:" ,self.playersturn, "Bowl:", bowl)
        #print("Opponentsturn", opponentsturn, "Bowl:", bowl)
        # Uncomment the 2 lines below to show what it looks like before the action
        #print("The current board look like:")
        #print(self.state)
        #Game().printboard()
        
        #We make a list contining only either players or the opponents 'opptions'
        #We only keep the goal of the current player since the player can't 
        #place anything in the other goal 
        #This also ordres the side of the current player
        board_state = self.state[self.playersturn] + self.state[opponentsturn]
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
        self.state[self.playersturn] = board_state[0:7]
        self.state[opponentsturn]=board_state[7:13] + [self.state[opponentsturn][-1]]
        #print(self.state)
        #Uncomment the 2 below to see the board after the action
        #print("The new state is")
        #print(state)) 
        
        #If bowl is empty the player can steel the opponents balls form the opposite bowl
        #the state of the current ball should equal 0 since it will mean that it was empty
        #before placing the last ball in the bowl. 
        #The bowl needs to be less than 6 since it will mean the player is on its own side
        #The last check to see if the opposite bowl has any balls in it. 
        if board_state[bowl] == 1 and bowl < 6 and board_state[bowl + ((5 - bowl) * 2 + 2)] > 0:
            #The plyer will get both it's one 1 ball as well as the one from the opponents bowl
            self.state[self.playersturn][-1] += self.state[self.playersturn][bowl]
            #self.state[self.playersturn][-1] += self.state[opponentsturn][bowl]
            self.state[self.playersturn][bowl] = 0
            #self.state[opponentsturn][bowl] = 0
    
            # Pocket index reversed due to anti-clockwise game
            bowl = abs(5 - bowl)
            if self.playersturn == 1:
                opponentsturn = 0
            else:
                opponentsturn = 1
            self.state[self.playersturn][-1] += self.state[opponentsturn][bowl]
            self.state[opponentsturn][bowl] = 0
            
        # Opponents turn if we are not in the goal, or else it is the players turn again
        if bowl != 6: 
            self.playersturn = opponentsturn
        else: 
            self.playersturn
        
        #print("The new state is")
        #print(self.state) 
    
        return True
    
    def printboard(self):
        #Game().get_state()
        if self.playersturn == 1:
            print()
            print("It's the upper plyers turn")
            print()
        else:
            print()
            print("It's the lower plyers turn")
            print()
        print("Bowls:             6  5  4  3  2  1 ")
        print("Upper Player:    ", list(reversed(self.state[1][0:-1])))
        print("Goals          ",self.state[1][-1:], "              ", self.state[0][-1:])
        print("Lower Player :   ", self.state[0][0:-1])
        print("Bowls:             1  2  3  4  5  6 ")
        #print("Lower Player", self.state[0][-1])

    def emptyside(self):
        #If one side is empty then the game will be done, we therefore check for this. 
        #If the players side is empty the remining balls on the opponents side will be added to it's goal
        if sum(self.state[0][0:-1]) == 0:
            self.state[1][-1] += sum(self.state[1][0:-1])
            return True
        if sum(self.state[1][0:-1]) == 0:
            self.state[0][-1] += sum(self.state[0][0:-1])
            return True
        
        return False
    
    def final_score(self):
        print()
        upper_player = self.state[1][-1]
        lower_player = self.state[0][-1]
        print("Upper player has:", upper_player, "points")
        print("Lower player has:", lower_player, "points")
        if upper_player > lower_player:
            print("Winner is Upper Player")
        elif lower_player > upper_player:
            print("Winner is Lower Player")
        else:
            ("It was a draw")
            
        
 

class Tree:
    def __init__(self, depth):
        self.depth = depth
        self.root = None
    def root(self, root):
        self.root = root

       
        
            

"""Test section """
game=Game()      

#while(!game.emptyside()):
    
#game.printboard()
#game.choose_bowl(3)
#game.printboard()
#game.choose_bowl(4)
#game.printboard()

game.printboard()

#"""
while not(game.emptyside()):
    input_bowl = int(input("What bowl do you choose "))
    game.choose_bowl(input_bowl)
    game.printboard()
#"""

game.final_score()
print("End of game")







      
        
        
        
        
        
        
          
        
    

