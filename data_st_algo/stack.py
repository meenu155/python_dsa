from collections import deque
#stack implementation in python with lists
stack=[]
stack.append('Hello World')
stack.append('I am ')
stack.append('Joseph Morgan')
print(stack.pop())#the element will be printed -Joseph Morgan
#implementation using deque
stack=deque()
stack.append(5)
stack.append(0)
stack.append(-2)
print(stack.pop())#will give last element which is -2 here


