#shell sort
def shellsort(arr):
    sublistcount=len(arr)//2
    while sublistcount>0:
        for start_position in range(sublistcount):
            gap_Insertionsort(arr, start_position, sublistcount)
        
        print("After increments of size ", sublistcount, "The list is ", arr)
        sublistcount=sublistcount//2
    return arr
        
def gap_Insertionsort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        current_value=arr[i]
        position=i
        
        while position>= gap and arr[position-gap]>current_value:
            arr[position]=arr[position-gap]
            position=position-gap
        arr[position]=current_value
    return arr
