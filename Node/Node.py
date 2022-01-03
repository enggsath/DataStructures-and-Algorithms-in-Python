class Node :
    #initializing a Node
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node
    #set next_node to the node
    def set_next_node(self,next_node):
        self.next_node = next_node
    #get current node_data
    def get_value(self):
        return self.value
    #get cuurent_node's next_node
    def get_next_node(self):
        return self.next_node
        
