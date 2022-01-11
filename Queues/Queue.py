import sys
sys.path.insert(0,"/home/f_k/Desktop/DSA/Node")#sys.path.insert(0,"Dir of where our Node class resides")
from Node import Node

class Queue:
    #initiate Queue to add upto max_size
    #max_size = None means bounded queue 
    def __init__(self,max_size=None):
        self.head=None
        self.tail=None
        self.max_size=max_size # property that bounded queues can utilize to limit the total node count
        self.size=0 #property to keep track of the queue’s current size

    #methoda that related to the size of the queue
    def get_size(self):
        return self.size
    def has_size(self):
        if(self.max_size != None):
            return self.max_size > self.get_size()
        return True
    def is_empty(self):
        return self.get_size() == 0
    
    #“Enqueue” is a fancy way of saying “add to a queue,” 
    def enqueue(self, value):
        new_Node=Node(value)
        if(self.has_size()):
            print(f"adding {value} to queue")
            if(self.is_empty()):
                self.head=new_Node
                self.tail=new_Node
            else:
                self.tail.set_next_node(new_Node)
                self.tail=new_Node
            self.size+=1
        else:
            print("Sorry, no more room!")
    
    #"dequeue" deltes first node/head_node from the queue and returns the value
    def dequeue(self):
        dequeue_node=self.head
        if(self.size>0):
            print(f"Removing {self.head.get_value()} from the queue")
            if(self.get_size()==1):
                self.tail=None
                self.head=None
            else:
                self.head=self.head.get_next_node()
            self.size-=1
        else:
            print("Sorry,This Queue is Empty>Can't dequeue")
        return dequeue_node.get_value()

    # allow us to view the value of head of the queue without returning it
    def peek(self):
        if(self.is_empty()):
            return None
        else:
            return self.head.get_value()

