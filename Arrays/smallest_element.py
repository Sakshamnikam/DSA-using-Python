def smallest_ele(arr):
    n=len(arr)
    smallest_ele=arr[0]
    sec_smallest=0
    for i in range(n):
        if (arr[i]<smallest_ele):
            smallest_ele=arr[i]
            

    return smallest_ele    
    





arr=[12,35,-1,10,10,34,1]
print(smallest_ele(arr))