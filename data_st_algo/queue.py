#single queue
class Queue:
    def __init__(self, max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def set_max_size(self,max_size):
        self.__max_size=max_size

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__rear==self.get_max_size()-1:
            # print("The queue is full.")
            return True
        else:
            return False

    def is_empty(self):
        if self.__front>self.__rear:
            # print("The queue is empty.")
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data

    def dequeue(self):
        if self.is_empty():
            print("The queue is empty")
        else:
            data=self.__element[self.__front]
            self.__front+=1
            return data
        
    def display(self):
        for i in range(self.__front, self.__rear+1):
            print(self.__element[i])

q=Queue(5)
q.enqueue(5)
q.enqueue(9)
q.enqueue(2)
q.dequeue()
print("The popped value is", q.dequeue())
q.display() 
"""
class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue)==0:
            return None
        else:
            self.queue.pop(0)
    def display(self):
        print(self.queue)
    def size(self):
        return len(self.queue)
q=Queue()
q.enqueue(4)
q.enqueue(9)
q.enqueue(7)
q.enqueue(7)
q.enqueue(2)
q.enqueue(0)
q.display()
q.dequeue()#deleted first element
q.display()
"""

