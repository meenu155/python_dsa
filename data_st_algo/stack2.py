class Stack:
    def __init__(self, max_size):
        self.__max_size=max_size
        self.__element=[None]*self.__max_size
        self.__top=-1

    def set_max_size(self,max_size):
        self.__max_size=max_size

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top==self.get_max_size()-1:
            return True
        else:
            return False

    def is_empty(self):
        if self.__top==-1:
            return True
        return False

    def push(self, data):
        if self.is_full():
            print("Stack is full")
        else:
            self.__top+=1
            self.__element[self.__top]=data

    def pop(self):
        if self.is_empty():
            print("The stack is empty")
        else:
            data=self.__element[self.__top]
            self.__top-=1
            return data
        
    def display(self):
        for i in range(self.__top+1):
            print(self.__element[i])

s=Stack(5)
s.push(5)
s.push(9)
s.push(2)
s.pop()
print("The popped value is", s.pop())
s.display()

