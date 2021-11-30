#Selection sort
def SelectionSort(arr):
    for i in range (len(arr)-1,0,-1):
        maxpos=0
        for j in range(1,i+1):
            if arr[j]>arr[maxpos]:
                maxpos=j

        temp=arr[i]
        arr[i]=arr[maxpos]
        arr[maxpos]=temp
    return arr
arr=[1,2,4,2,5,7,2,5,9,3]
print(SelectionSort(arr))
