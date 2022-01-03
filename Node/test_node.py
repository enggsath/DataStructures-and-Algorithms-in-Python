#from Node.py import Node class
from Node import Node
#creating Node instances
Node_a=Node("Apple")
Node_b=Node("Ball")
Node_c=Node("Cat")

#setting links
Node_a.set_next_node(Node_b)
Node_b.set_next_node(Node_c)

#retreving Node_c data from Node_a
print(Node_a.get_next_node().get_next_node().get_value())
#retreving Node_c data from Node_b
print(Node_b.get_next_node().get_value()) 