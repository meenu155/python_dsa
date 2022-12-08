def merge(A,l,mid,r,b):
    i=l
    j=mid+1
    k=l
    while i<=mid and j<=r:
        if A[j]>A[i]:
            b[k]=A[i]
            i=i+1
        else:
            b[k]=A[j]
            j=j+1
        k=k+1
    if i>mid:
        while j<=r:
            b[k]=A[j]
            k=k+1
            j=j+1
    if j>r:
        while i<=mid:
            b[k]=A[i]
            k=k+1
            i=i+1
    for i in range(l,r+1):
        A[i]=b[i]

def mergesort(A,l,r,b):
    if l<r:
        mid=(l+r)//2
        mergesort(A,l,mid,b)
        mergesort(A,mid+1,r,b)
        merge(A,l,mid,r,b)
A=[5,4,3,2,1]
b=[0]*len(A)
l=0
r=len(A)-1
mergesort(A,l,r,b)
print(b)
