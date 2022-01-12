import sys
sys.path.insert(0,"/home/f_k/Desktop/DSA/Node")
from Node import Node

class Stack:
  def __init__(self,name):
    self.top_item = None
    self.size = 0
    self.limit =1000
    self.name=name
  #add a value to stack;top of stack
  def push(self, value):
    if(self.has_space()):
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size+=1
    else:
      print("All out of space!")
    #remove a value from stack;removes val/node @ top_of_stack
  def pop(self):
    if self.size > 0:
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This stack is totally empty.")
  
  #returns the top node of the stack
  def peek(self):
    if (self.size <= 0):
        print("Nothing to see here!")
        return None
    return self.top_item.get_value()
   
  # Define has_space() and is_empty() below:
  def has_space(self):
    return self.size<self.limit
  def is_empty(self):
    return self.size==0

  #size of stack
  def get_size(self):
    return self.size
    
  #get name of stack frame
  def get_name(self):
    return self.name
  #print items in stack frame
  def print_items(self):
    pointer = self.top_item
    print_list = []
    while(pointer):
      print_list.append(pointer.get_value())
      pointer = pointer.get_next_node()
    print_list.reverse()
    print("{0} Stack: {1}".format(self.get_name(), print_list))