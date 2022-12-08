"""n=int(input())
arr=[]
def ntostr(n,arr):
    if n==0:
        return arr
    else:
        arr.append(n%10)
        ntostr(n//10,arr)
ntostr(n,arr)
print(arr)
arr.reverse()
d={0:'zero',1:'one',2:'two',3:'thre',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
for i in range(len(arr)):
    arr[i]=d[arr[i]]
print(*arr)
"""
# check sorted
"""
def issorted(a,size):
    print(a)
    print(size)
    if size==0 or size==1:
        return True
    if  a[0]>a[1]:
        print(a[0])
        return False
    else:
        a=a[1:]
        size=len(a)
        return issorted(a,size)
n=int(input('enter the size of the list'))
a=list(map(int,input().split()))
b=issorted(a,n)
print(b)

#give sum of the given list
def getsum(a,s):
    if len(a)==0:
        return 0
    if len(a)==1:
        return a[0]
    else:
        s=s+a[0]
        a=a[1::]
        return s+getsum(a,s)
s=0
a=list(map(int,input().split()))
t=getsum(a,s)
print(t)
"""
#print your name n times
#this is showing backtracking
from calendar import weekday


def nt(s,t):
    if t==0:
        return
    else:
        nt(s,t-1) 
        print(s)    
nt('Meenu',4)
# print 1 to n with backtracking
def lin(n):
    if n==0:
        return
    lin(n-1)
    print(n)
lin(100)
#print n to 1 y backtracking
def nto(i,n):
    if i>n:
        return 
    nto(i+1,n)
    print(i)
nto(1,10)
#summation of first n numbers
#parametrized method
def summ(s,n):
    if n<1:
        print(s)
        return 
    summ(s+n,n-1)
summ(0,3)
#functional way
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
a=sum(3)
print(a)
#swapping number
def swap(l,r):
    if l<=r:
        a[l],a[r]=a[r],a[l]
        swap(l+1,r-1)
a=[1,2,3,4,6]
swap(0,4)
print(a)
#palindrome
def checkpalindrome(i,n,s):
    if i>=n//2:
        return True
    elif s[i]!=s[n-i-1]:
        return False
    else:
        return checkpalindrome(i+1,n,s)
print(checkpalindrome(0,5,'madam'))
print(checkpalindrome(0,6,'mmbbmm'))
print(checkpalindrome(0,4,'acda'))


