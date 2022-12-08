from queue import Queue
visited={}
level={}
parent={}
bfs_output=[]
queue=[]
adj_list={'5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []}
for node in adj_list.keys():
    visited[node]=False
    level[node]=-1
    parent[node]=None
s='5'
visited[s]=True
level[s]=0
queue.append(s)
while len(queue)!=0:
    u=queue.pop(0)
    bfs_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            level[v]=level[u]+1
            parent[v]=u
            queue.append(v)
print(bfs_output)
print(level)






