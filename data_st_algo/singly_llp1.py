#linked list
#1creating of node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#2class singly
class SinglyLL:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head==None:
            print('Linked List is empty')
        else:
            a=self.head
            while a is not None:
                print(a.data ,end=" ")
                a=a.next
    def insertatbeg(self,data):
        print()#did this for next line
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insertatend(self,data):
        print()
        ne=Node(data)
        a=self.head#head of linked list we made object of this class
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.next=None
    def insertatanypoint(self,data,position):
        na=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        na.next=a.next
        a.next=na
    def delatb(self):
        a=self.head
        self.head=a.next
        a.next=None
    def delate(self):
        a=self.head
        while a.next is not None:
            prev=a
            a=a.next
        prev.next=None
    def delanynode(self,position):
        a=self.head
        for i in range(1,position-1):
            a=a.next
        b=a.next
        a.next=b.next
        b.next=None
    def lreversal(self):
        curr=self.head
        prev=None
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        self.head=prev
n1=Node(1)      
l1=SinglyLL()
l1.head=n1
n2=Node(3)
n1.next=n2
n3=Node(7)
n2.next=n3
l1.traversal()
#insertion
#insertion at the beg
l1.insertatbeg(9)
l1.traversal()
l1.insertatend(11)
l1.traversal()
print()
l1.insertatanypoint(15,3)
l1.traversal()
print()
l1.delatb()
l1.traversal()#we see 9 is deleted which was the first element
print()
l1.delate()
l1.traversal()
print()
l1.delanynode(3)
l1.traversal()
print()
l1.lreversal()
l1.traversal()

        
    
    
