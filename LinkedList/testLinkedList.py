# from LinkedList file/module import LinkedList class
from LinkedList import LinkedList

#creating a linked list
L1=LinkedList()
L1.add_new(5)
L1.add_new(23)
L1.add_new("Sita")
L1.add_new("Rama")
L1.add_new(23.45)

#print L1 linked list
print("linked list before removing")
print(L1.stringify_list())
#remove 23 from L1 linked list
L1.remove_node(23)
#print L1 LinkedList after removing
print("linked list after removing")
print(L1.stringify_list())

#retrive head_node
print(L1.get_head_node())