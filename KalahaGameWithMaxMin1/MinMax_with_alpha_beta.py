# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:46:57 2022

@author: aksel
"""
import copy

## needs to iport node/leaf from tree generated every turn
from AI import leaf
from kalahaGame import game

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
        
    def Max(self, node, a, b, current_depth):
        
        
        ##Make terminal check
        util_terminal = self.terminal_test(node, leaf, current_depth)
        if util_terminal > 0:
            return util_terminal
        
        # get data from tree
        data = node.get_tree_data
        
        #init value
        value =float ('-inf')
        
        ##Look trhough all actions (children of the node)
        for i in node.get_children():
            c_data = copy(data) ##Make a copy of current game
            
            #Max func if AI, and min func if player
            res_node = self.result(node, i)
            
            if game.get_playersturn()== 1:
                value = max(value, self.Max(res_node, a, b, current_depth + 1))
            else:
                value = max(value, self.Min(res_node, current_depth + 1))
        
            ##something with alpha beta
            
            ## Reset game state, so the next itteration works with the correct node
            node.set_game(c_data)
            
    def Min(self,node, a, b, current_depth):
        #Min is more or less just a copy of max, but taking min values ofcourse
        ##Make terminal check
        util_terminal = self.terminal_test(node, leaf, current_depth)
        if util_terminal > 0:
            return util_terminal
        
        # get data from tree
        data = node.get_tree_data
        
        #init value
        value =float ('-inf')
        
        ##Look trhough all actions (children of the node)
        for i in node.get_children():
            c_data = copy(data) ##Make a copy of current game
            
            #Max func if AI, and min func if player
            res_node = self.result(node, i)
            
            if game.get_playersturn()== 1:
                value = min(value, self.Max(res_node, a, b, current_depth + 1))
            else:
                value = min(value, self.Min(res_node, a, b, current_depth + 1))
        
            ##something with alpha beta
            
            ## Reset game state
            node.set_game(c_data)
    def alpha_beta(self, tree):
        value , itteration = self.Max(tree.root, float('-inf'), float('inf'), current_depth =0)
        
        
        
        
        
        
        