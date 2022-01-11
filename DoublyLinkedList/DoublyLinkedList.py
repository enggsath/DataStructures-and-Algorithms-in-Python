from Node import Node
'''
Depending on the end-use of the doubly linked list, there are a variety of methods that we can define.
'''
class DoublyLinkedList:
    #initialize the list with constructor
    def __init__(self):
        self.head_node = None
        self.tail_node = None
    #Add a new node to the head (beginning) of the list
    def add_to_head(self,new_value):
        New_head=Node(new_value)
        current_head=self.head_node
        if(current_head != None):
            New_head.set_next_node(current_head)
            current_head.set_prev_node(New_head)
        self.head_node=New_head
        if(self.tail_node == None):
            self.tail_node=New_head
    
    #Add a new node to the tail(end) of the list
    def add_to_tail(self,new_value):
        new_tail=Node(new_value)
        current_tail=self.tail_node
        if(current_tail!=None):
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        self.tail_node=new_tail
        if(self.head_node == None):
            self.head_node=new_tail
    
    #Remove head_node from the DoublyLinkedList
    def remove_head(self):
        removed_head=self.head_node
        if(removed_head==None):
            return None
        self.head_node=removed_head.next_node
        self.head_node.set_prev_node(None)
        if(removed_head==self.tail_node):
            self.remove_tail()
        return removed_head.get_value()

    #remove tail_node from the linked list
    def remove_tail(self):
        removed_tail=self.tail_node
        if(removed_tail==None):
            return None
        self.tail_node=removed_tail.get_prev_node() 
        self.tail_node.set_next_node(None)
        if(removed_tail==self.head_node):
            self.remove_head()
        return removed_tail.get_value()

    #remove node by value
    def remove_by_val(self,value_to_remove):
        node_to_remove=None
        current_head=self.head_node
        while current_head!=None:
            if(current_head.get_value()==value_to_remove):
                node_to_remove=current_head
                break
            current_head=current_head.get_next_node()
        #if we there is no value matched in our node's value, then
        if(node_to_remove==None):
            return None
        elif(node_to_remove==self.head_node):
            self.remove_head()
        elif(node_to_remove==self.tail_node):
            self.remove_tail()
        else:
            next_node=node_to_remove.get_next_node()
            prev_node=node_to_remove.get_prev_node()
            prev_node.set_next_node(next_node)
            next_node.set_prev_node(prev_node)
        return node_to_remove.get_value()

    #traverse the list and print list items
    def stringify_list(self):
        current_node=self.head_node
        st=''
        while current_node != None:
            st+=str(current_node.get_value())+"\n"
            current_node=current_node.get_next_node()
        return st
    

