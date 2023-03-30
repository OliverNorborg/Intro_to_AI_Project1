# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:29:59 2022

@author: aksel
"""
import copy
from KalahaGame import Game

class Node:
    def __init__(self, data):
        self.data = data
        self.child = {}
    def addchild(self, action, child):
        self.child[action] = child
    def getchild(self):
        return self.child
    def adddata(self, data):
        self.data = data
    def getdata(self):
        return self.data
    def action(self, i):
            Game().choose_bowl(i)

class Leaf:
    def __init__(self, data):
        self.data = data
    def getdata(self):
        return self.data

class Tree:
    def __init__(self, max_depth=5):
        #Set max_depth to an integer 
        self.max_depth = max_depth
        self.root = None
    def root(self, root):
        self.root = root
    def build_tree(self, node, recursion):
        #Will be a recursion function that adds all the nodes until
        #the max depth is reached 
        if recursion > self.max_depth:
            return
        #Add children (nodes) for all the possible movesd #5 different bowls
        i = 1
        for i in range(5):
            board = copy.deepcopy(Node(node).getdata()) #These nodes will all be siblings
            #print("board", board)
            if Game().choose_bowl(i+1):
                #print("Bowl", i+1)
                Game().printboard()
                if not Game().emptyside():
                    Node(node).addchild(action=i, child=Leaf(board))
                else:
                    Node(node).addchild(action=i, child=Node(board))
                    #print("action",i)
                    #print("child", Node(board))
        for child in range(len(Node(node).getchild())):
            #Check if a child is a node
            if isinstance(child, Node):
                self.build_tree(child, recursion + 1)
                
   