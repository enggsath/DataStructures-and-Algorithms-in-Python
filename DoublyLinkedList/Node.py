''' doubly linked list, the nodes have pointers to the previous node as well as the next node. 
This means that the doubly linked list data structure has a tail property in addition to a head property, 
which allows for traversal in both directions.

So the nodes we will use for our doubly linked list contain three elements:

A value
A pointer to the previous node
A pointer to the next node
'''
#Update Node class for Doubly linked list nodes
class Node:
    def __init__(self,value,next_node=None,prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    #setters
    #set next_node pointer to next node
    def set_next_node(self,next_node):
        self.next_node =next_node
    #set prev_node pointer to previous node
    def set_prev_node(self,prev_node):
        self.prev_node =prev_node

    #getters 
    #return node's value
    def get_value(self):
        return self.value
    #return node's next node
    def get_next_node(self):
        return self.next_node
    #return node's previous node
    def get_prev_node(self):
        return self.prev_node

