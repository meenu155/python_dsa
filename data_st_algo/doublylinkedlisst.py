class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_empty(self, data):
        nn=Node(data)
        if self.head is  None:
            self.head=nn
        else:
            print("The list is not empty")

    def insert_beginning(self, data):
        nn=Node(data)
        if self.head is None:
            print("The list is empty")
        else:
            nn.next=self.head
            self.head.prev=nn
            self.head=nn

    def insert_end(self, data):
        nn=Node(data)
        if self.head is None:
            print("The list is empty")
        else:
            tmp=self.head
            while(tmp.next is not None):
                tmp=tmp.next
            tmp.next=nn
            nn.prev=tmp

    def add_after(self, data, data_before):
        nn=Node(data)
        if self.head is None:
            print("The list is empty")
        else:
            tmp=self.head
            while(tmp.next is not None):
                if tmp.data==data_before:
                    break
                tmp=tmp.next
            if tmp is None:
                print(data_before,"not found")
            else:
                nn.next=tmp.next
                nn.prev=tmp
                if tmp.next is not None:
                    tmp.next.prev=nn
                tmp.next=nn

    def forward_traversal(self):
        print("Forward Traversal")
        if self.head is None:
            print("The list is empty")
        else:
            tmp=self.head
            while(tmp is not None):
                print(tmp.data)
                tmp=tmp.next

    def backward_traversal(self):
        print("Backward Traversal")
        if self.head is None:
            print("The list is empty")
        else:
            tmp=self.head
            while(tmp.next is not None):
                tmp=tmp.next

            while tmp is not None:
                print(tmp.data)
                tmp=tmp.prev
            

d=DLL()
d.insert_empty(30)
d.insert_beginning(3)
d.insert_end(60)
d.add_after(50, 30)
d.add_after(90, 60)
d.forward_traversal()
d.backward_traversal()