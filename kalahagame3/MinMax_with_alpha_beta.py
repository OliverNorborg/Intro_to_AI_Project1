# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:46:57 2022

@author: aksel
"""
import copy

## needs to iport node/leaf from tree generated every turn
from tree_builder import Leaf, Node ## Assuming that we have an AI file, and a leaf in the tree
from KalahaGame import Game

game = Game()

class MinMax:
    
    def _init_(self, utility_func, result, max_depth):
        self.utility_func = utility_func
        self.result = result
        self.max_depth = max_depth
    
    def terminal_test(self, node, leaf, current_depth):
        ## If the final game state is game over, or is of max depth
        ## calculate the utility
        if isinstance(node, leaf) or current_depth >= self.max_depth:
            ## calculate the utility based on the evaluation func from node
            utility = node.cal_util(self.utility_func), 0
            return utility
        
    def Max(self, node, current_depth, first_branch, second_branch):
        
        
        ##Make terminal check
        util_terminal = self.terminal_test(node, Leaf, current_depth)
        if util_terminal > 0:
            return util_terminal
        
        # get data from tree
        data = node.getdata()
        
        #init value
        value =float ('-inf')
        best_move = -1
        
        ##Look trhough all actions (children of the node)
        for i in node.getchildren():
            c_data = copy(data) ##Make a copy of current game
            
            #Max func if AI, and min func if player
            res_node = self.result(node, i)
            
            if game.get_playersturn()== 1:
                value = max(value, self.Max(res_node, current_depth + 1, first_branch, second_branch))
            else:
                value = max(value, self.Min(res_node, current_depth + 1 , first_branch, second_branch))
        
        
            ## Reset game state, so the next itteration works with the correct node
            node.reset_game(c_data)
            
            ##do alpha beta pruning of the branches
            
            if value >= second_branch:
                return value, best_move
            if value > first_branch:
                best_move = i
                
            first_branch = max(first_branch, value)
        
        return value, best_move
    
            
        
            
            
            
    def Min(self,node, current_depth, first_branch, second_branch):
        #Min is more or less just a copy of max, but taking min values ofcourse
        ##Make terminal check
        util_terminal = self.terminal_test(node, Leaf, current_depth)
        if util_terminal > 0:
            return util_terminal
        
        # get data from tree
        data = node.get_tree_data
        
        #init value
        value =float ('-inf')
        best_move = -1
        
        ##Look trhough all actions (children of the node)
        for i in node.getchildren():
            c_data = copy(data) ##Make a copy of current game
            
            #Max func if AI, and min func if player
            res_node = self.result(node, i)
            
            if game.get_playersturn()== 1:
                value = min(value, self.Max(res_node, current_depth + 1, first_branch, second_branch))
            else:
                value = min(value, self.Min(res_node, current_depth + 1, first_branch, second_branch))
        
            ## Reset game state, so the next itteration works with the correct node
            node.reset_game(c_data)
            
            ##do alpha beta pruning of the branches
            
            if value <= first_branch:
                return value, best_move
            if value > second_branch:
                best_move = i
                
            second_branch = min(second_branch, value)
        
        return value, best_move
    def alpha_beta(self, tree):
        value , itteration = self.Max(tree.root, float('-inf'), float('inf'), current_depth =0)