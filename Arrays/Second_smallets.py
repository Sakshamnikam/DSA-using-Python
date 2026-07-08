def second_smallest(arr):
    n=len(arr)
    smallest=float('inf')
    second_smallest=float('inf')

    for i in range(n):
        if(arr[i]<smallest):
            second_smallest=smallest
            smallest=arr[i]
            
       
        
        
    return second_smallest

arr=[-10,-12,-18,-42,-6,-1]
print(arr)
print(second_smallest(arr))