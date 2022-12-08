
def heapify(a,n,largest):
    i=largest
    left=2*i+1
    right=2*i+2
    if left<n and a[left]>a[largest]:
        largest=left
    if right<n and a[right]>a[largest]:
        largest=right
    if largest!=i:
        a[largest],a[i]=a[i],a[largest]
        heapify(a,n,largest)
def heapsort(a):
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        heapify(a,i,0)
a=[2,15,4,30,18,6,25]
n=len(a)
for i in range(n//2-1,-1,-1):
    heapify(a,n,i)
heapsort(a)
print(a)


    
