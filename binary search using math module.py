#binary search
import math
def bin_search(lis,element):
    bottom=0
    top=len(lis)-1
    index=-1
    while top>= bottom and index==-1:
        mid=int(math.floor((top+bottom)/2))
        if lis[mid]==element:
            index = mid
        elif lis[mid]>element:
            top =mid-1
        else:
            bottom=mid+1
    return index
lis=[2,3,4,5,6,7,8]
print(bin_search(lis,4))
