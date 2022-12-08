#multiple function calls
#fibonacci series 0,1,1,2,3.... 0th is 0
"""
def fun(n):
    if n<=1:
        return n
    last=fun(n-1)
    slast=fun(n-2)
    return last + slast
a=fun(3)
print(a)
#so we must understand what is a subsequence a subsequence is 321
# so 312 can not be a subsequence as order is not mainatained but 31 and 32 can be
print('printing subsequence')
l=[]
arr=[3,1,2,4,5]
i=0
def f(i,l):
    if i>=len(arr):
        print(l)
        return
    l.append(arr[i])
    f(i+1,l)
    l.pop()
    f(i+1,l)
#print all subsequences with sum==k
f(0,l)  
def f(l,nums,i,s,k):
    if i>=len(nums):
        if s==k:
            print(l)
        return
    l.append(nums[i])
    s=s+nums[i]
    f(l,nums,i+1,s,k)
    l.pop()
    s=s-nums[i]
    f(l,nums,i+1,s,k)
nums=[1,2,3]
i=0
k=4
s=0
l=[]
ans=f(l,nums,i,s,k)
#print any onse subsequeence whose sum is k
def f(l,nums,i,s,k):
    if i>=len(nums):
        if s==k:
            print(l)
            return True
        else:
            return False
    l.append(nums[i])
    s=s+nums[i]
    if f(l,nums,i+1,s,k)==True:
        return True
    l.pop()
    s=s-nums[i]
    if f(l,nums,i+1,s,k)==True:
        return True
    return False
nums=[1,2,1]
i=0
k=2
s=0
l=[]
ans=f(l,nums,i,s,k)
#print count of subsequences whose sum==k
def f(nums,i,s,k):
    if i>=len(nums):
        if s==k:
            return 1
        else:
            return 0
    s=s+nums[i]
    l1=f(nums,i+1,s,k)
    s=s-nums[i]
    r=f(nums,i+1,s,k)
    return l1+r
nums=[1,2,1]
i=0
k=2
s=0
l=[]
ans=f(nums,i,s,k)
print(ans)""" 
def f(l,nums,i,s,k):
    if i>=len(nums):
        if s==k:
            print(l)
        return
    l.append(nums[i])
    s=s+nums[i]
    f(l,nums,i+1,s,k)
    l.pop()
    s=s-nums[i]
    f(l,nums,i+1,s,k)
nums=[1,1,1,1,2,2]
i=0
k=4
s=0
l=[]
ans=f(l,nums,i,s,k)



