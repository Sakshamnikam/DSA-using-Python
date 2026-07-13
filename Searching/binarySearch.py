
def binary_search(ls,x):
    low=0
    high=len(ls)-1

    while low<=high:
        mid=low+(high-low)//2

        if (ls[mid]==x):
            return mid
        elif ls[mid]<x:
            low = mid + 1
        else:
            high = mid - 1
    return -1        

ls=[1,2,3,4,5] 
res=binary_search(ls,5)
if(res<0):
    print('Not found!')
else:
    print('Element found at index :',res)