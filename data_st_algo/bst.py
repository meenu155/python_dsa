#BST
class BST:
    def __init__(self,data):
        self.key=data
        self.rchild=None
        self.lchild=None
    def insert_node(self,data):
        if self.key==data:
            print('the tree is empyty')
        if self.key>=data:
            if self.lchild:
                self.lchild.insert_node(data)
            else:
                self.lchild=BST(data)
        if self.key<data:
            if self.rchild:
                self.rchild.insert_node(data)
            else:
                self.rchild=BST(data)
    def iterativeSearch(self, data):
        temp=self
        while temp!= None:
            if data > temp.key:
                temp = temp.rchild
            elif data< temp.key:
                temp = temp.lchild
            else:
                return True
        return False
def preorder(self):
    if not self:
        return
    print((self.key))
    self.preorder(self.lchild)
    self.preorder(self.rchild)
r=BST(20)
print(r.key)
print(r.rchild)
print(r.lchild)
r.insert_node(1)
r.insert_node(7)
r.insert_node(5)
r.insert_node(3)
r.insert_node(4)
print(r.iterativeSearch(7))






