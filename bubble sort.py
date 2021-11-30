 #bubble sort

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr
arr=[3,5,3,7,2,9,1,3,5,7]
print(bubbleSort(arr))
