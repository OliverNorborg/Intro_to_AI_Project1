#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:36:22 2022

@author: olivernorborg
"""

from KalahaGame import Game

class utility:
    def calc_utility(playersturn, state):
        #initialize the utility variable
        utility = 0
        if playersturn == 1:
            opposite_player = 0
        else:
            opposite_player = 1
        
        for bowl, balls in enumerate(state[playersturn][0:6]):
            #We go through each state and look at how many balls are in each bowl
            #If balls in the bowl equal the amount of bowl we fill until we reach
            #out scoring it will be am extra turn
            #Example from init state
            #bowl 1 (in the list it will be nuber 0) has 6 balls so 6-0=6 and is therefore
            #an extra turn 
            if(6-bowl) == balls:
                #Then we check if its the curret playersturn or the opponets turn
                #if its the player board side the utility is added with 6 if its the 
                #opponents board side then the utility is subtracted with 6. 
                if playersturn == 1:
                    utility += 6
                else:
                    utility += -6
            #We then check if the move will result in a ball in the players goal. 
            #Or in the opponents goal - this does not weigth as much as an extra turn
            if balls > (6-bowl):
                if playersturn == 1:
                    utility += 2
                else:
                    utility += -2
            # We then check if there are 13 or more balls
            if balls >= 13:
                if playersturn == 1:
                    utility += 1
                else:
                    utility += -1
            #Lastly we check if there are piece to 'steel'
            #first we check if the balls we take from the bowl will end in an empty bowl
            #utilit will be 3. 
            
            
        
        return utility
        
    def utility_func():
        #initialize for calculation everytime we call the function and reset
        #utilit to zero 
        utility = 0 
        state = Game().get_state()
        playersturn = Game().get_playersturn()
        if playersturn == 1:
            opposite_player = 0
        else:
            opposite_player = 1
        
        utility += utility().calc_utility(playersturn, state)
        utility += utility().calc_utility(opposite_player, state)

        return utility