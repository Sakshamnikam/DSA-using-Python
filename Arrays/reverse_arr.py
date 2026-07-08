def reverse_arr(arr):
    n=len(arr)

    temp=[0]*n

    for i in range(0,n):
        temp[i]=arr[n-i-1]
    for i in range(0,n):
        arr[i]=temp[i]

    return arr

arr=[12,35,-1,10,10,34,1]

print(reverse_arr(arr))
