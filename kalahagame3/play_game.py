# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:59:07 2022

@author: aksel
"""
from tree_builder import Tree, Leaf, Node ## Assuming that we have an AI file, and a leaf in the tree
from KalahaGame import Game
from MinMax_with_alpha_beta import MinMax


game = Game()
game.printboard()
tree = Tree( )
root = Node(game.get_state())

while not(game.emptyside()):
    
    if game.turn() == 0:
        input_bowl = int(input("What bowl do you choose "))
        game.choose_bowl(input_bowl)
        game.printboard()
    else:
        #input_bowl = int(input("What bowl do you choose "))
        print("AI is moving")
        print(game.get_state())
        root = Node(game.get_state())
        tree.build_tree(root, 0)
        #Change input in choose bowl to what every bowl the min max algorithm gets 
        game.choose_bowl(2)
        game.printboard()

game.final_score()
print("End of game")