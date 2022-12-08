# Python3 program to demonstrate working of heapq

from heapq import heapify, heappush, heappop
import heapq
 
# initializing list
li = [5, 7, 9, 1, 3]
 
# using heapify to convert list into heap
heapq.heapify(li)
 
# printing created heap
print("The created heap is : ", end="")
print(list(li))
 
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li, 4)
 
# printing modified heap
print("The modified heap after push is : ", end="")
print(list(li))
 
# using heappop() to pop smallest element
print("The popped and smallest element is : ", end="")
print(heapq.heappop(li))
print(li)
for i in range(len(li)):
	print(i)
while len(li)>1:
	a=heapq.heappop(li)
	print(a)

