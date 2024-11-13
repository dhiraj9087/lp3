def deterministic_par(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def determisitic_quick(arr,low,high):
    if low<high:
        pi=deterministic_par(arr,low,high)
        determisitic_quick(arr,low,pi-1)
        determisitic_quick(arr,pi+1,high)


import random
def random_par(arr,low,high):
    pivot = random.randint(low,high)
    arr[pivot],arr[high]=arr[high],arr[pivot]
    return deterministic_par(arr,low,high)

def random_quick(arr,low,high):
    if low<high:
        pi = random_par(arr,low,high)
        random_quick(arr,low,pi-1)
        random_quick(arr,pi+1,high)
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

# Using Deterministic Quick Sort
# determisitic_quick(arr, 0, n - 1)
random_quick(arr,0,n-1)
print(arr)