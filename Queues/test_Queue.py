#creating a Queue for people in queue for cinema tickets with the queue size limited=N numbers
'''people  are entering in line to purchase tickets
We need to add to them to queue such that first entered person should get the ticekt and leave the queue once they got
At every time if a person leaves the queue,The person who at first in line name should be displayed 
'''

from Queue import Queue

n=int(input("# of persons to enter  queue >"))
ticket_Line=Queue(n)
for i in range(n):
    person=input("Enter the name of person >")
    ticket_Line.enqueue(person)
    
#issue tickets and remove first 2 persons and display their name
print(ticket_Line.dequeue())
print(ticket_Line.peek())