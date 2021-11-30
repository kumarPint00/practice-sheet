#Insertion sort
def InsertionSort(arr):
    for index in range(1,len(arr)):
        current_value=arr[index]
        position=index

        while position>0 and arr[position-1] > current_value:
            arr[position]=arr[position-1]
            position=position-1

        arr[position]=current_value

    return arr

arr=[1,2,1,1,2,39,9,2,5]
print(InsertionSort(arr))
