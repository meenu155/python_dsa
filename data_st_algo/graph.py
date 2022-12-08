all_edges=[('A','C'),('A','B'),('B','C')]
class Graph:
    def __init__(self,Nodes,is_directed):
        self.nodes=Nodes
        self.adjacency_list={}
        self.is_directed=is_directed
        for node in self.nodes:
            self.adjacency_list[node]=[]
    def print_adj_list(self):
        for node in self.nodes:
            print(node,'->',self.adjacency_list[node])
    def add_edge(self,u,v):
        self.adjacency_list[u].append(v)
        print(self.is_directed)
        if self.is_directed==False:
            self.adjacency_list[v].append(u)
Nodes=['A','B','C']
is_directed=input()
if is_directed=='True':
    is_directed=True
else:
    is_directed=False
graph1=Graph(Nodes,is_directed)
graph1.print_adj_list()
for u,v in all_edges:
    graph1.add_edge(u,v)
graph1.print_adj_list()

