'''Testing stack class'''

from stack import Stack

gym_stack=Stack(5)
gym_stack.push(100)
gym_stack.push(50)
gym_stack.push(25)
gym_stack.push(12)
gym_stack.pop()
gym_stack.push(10)

print(gym_stack.peek()) #returns 10

