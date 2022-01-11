'''
Before moving on, take a moment to think about doubly linked lists. 
What do you think are some possible real-life uses?

Some uses are:
->A music player with “next” and “previous” buttons
->An app that shows you where your subway is on the train line
->The “undo” and “redo” functionality in a web browser
'''

'''we’re going to use DoublyLInkedList class to model a subway line. A doubly linked list is a great 
data structure to use to model a subway, as both have a first and last element, 
and are comprised of nodes (or stops) with links to the elements before and after them'''

'''We’re going to model a (fictional) subway line that will travel from Central Park to the Brooklyn Bridge.
'''
#STEP 1
'''
The subway starts at Central Park and winds its way downtown. In the following order:
1."Times Square" to the head of the list
2."Grand Central" to the head of the list
3."Central Park" to the head of the list
'''#we use add_head method
#STEP 2
'''
The subway continues from Times Square down to the Brooklyn Bridge. In the following order:
4."Penn Station"
5."Wall Street"
6."Brooklyn Bridge"
'''#we use add_tail method to add from tail_node
#STEP 3
'''Oh no! There’s construction happening on the subway line: the Central Park and Brooklyn Bridge stops
 will temporarily be closed.Remove them from your list without iterating through the entire list
 '''#we use remove_head & tail methods here

 #STEP 4
'''It turns out that the Times Square station is under construction as well. 
    Remove it from the list
'''#we use remove_by_val method here to eleminate Times SQuare Station

from DoublyLinkedList import DoublyLinkedList as dll

subway=dll()
#step 1
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")
#step 2
subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
print(subway.stringify_list())
#Step 3
print(subway.remove_head())
print('\n')
print(subway.remove_tail())
#step 4
print('\n')

print(subway.remove_by_val("Times Square"))
print('\n')

print(subway.stringify_list())
