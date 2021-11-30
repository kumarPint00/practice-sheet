#sequential_search
def Sequential_search(arr, item):
    pos=0
    found=False
    while pos< len(arr) and not found:
        if arr[pos]==item:
            found=True
        else:
            pos +=1
    return found , pos
arr=[1,2,3,5,6,7]
print(Sequential_search(arr,0))
