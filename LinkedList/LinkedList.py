
import sys
#print(sys.path)   -->returns a list of directories where python files our modules for this program/file
#inserting out intended directory in sys.path,so that our program find it's Node module in Node directory
sys.path.insert(0,"/home/f_k/Desktop/DSA/Node")

#import Node module
from Node import Node

class LinkedList:
    #initializing LinkedList for given instance
    def __init__(self,value=None):
        self.head_node=Node(value)
    
    #add a Node at beginning of a LinkedList
    def add_new(self,new_value):
        New_node=Node(new_value)
        New_node.set_next_node(self.head_node)
        self.head_node=New_node
    
    #remove a Node from LinkedList
    def remove_node(self,remove_value):
        current_node=self.head_node
        if(current_node.get_value()==remove_value):
            self.head_node=current_node.get_next_node()
        else:
            while current_node:
                next_node=current_node.get_next_node()
                if(next_node.get_value()==remove_value):
                    current_node.set_next_node(next_node.get_next_node())
                    current_node=None
                else:
                    current_node=current_node.get_next_node()

    #Traverse through LinkedList
    def stringify_list(self):
        current_node=self.head_node
        string_list=''
        while current_node:
            string_list+=str(current_node.get_value())+" , "
            current_node=current_node.get_next_node()
        return string_list

    #retrive head_node of specified_Linked_list
    def get_head_node(self):
        return self.head_node.get_value()
