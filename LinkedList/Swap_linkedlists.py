import LinkedList

def swap_nodes(list,val1,val2):
    if(val1==val2):
        print('swapping is not necessary ,as both are same values')
        return
    print(f'swapping {val1} and {val2}')
    Node1=list.head_node
    Node2=list.head_node
    Node1_prev=None
    Node2_prev=None
    while Node1:
        if(Node1.get_value()==val1):
            break
        Node1_prev=Node1
        Node1=Node1.get_next_node()
    while Node2:
        if(Node2.get_value()==val2):
            break
        Node2_prev=Node2
        Node2=Node2.get_next_node()
    if(Node1==None or Node2==None):
        print('Swapping is not possible-one or more element is not in the list')
        return

    if Node1_prev==None:
        list.head_node=Node2
    else:
        Node1_prev.set_next_node(Node2)
    if(Node2_prev==None):
        list.head_node=Node1
    else:
        Node2_prev.set_next_node(Node1)

    temp=Node1.get_next_node()
    Node1.set_next_node(Node2.get_next_node())
    Node2.set_next_node(temp)

ll = LinkedList.LinkedList()
for i in range(10):
  ll.add_new(i)

print(ll.stringify_list())
swap_nodes(ll, 9, 5)
print(ll.stringify_list())
swap_nodes(ll, 12, 5)
print(ll.stringify_list())
swap_nodes(ll,5, 5)
print(ll.stringify_list())