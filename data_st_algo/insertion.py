#insertion sort
from tempfile import tempdir


def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while j >=0 and temp < arr[j] :
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    print(*arr)
arr=[5,3,2,1]
n=4
insertionSort(arr)


            
