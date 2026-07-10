def rotateArr(arr,d):

    n=len(arr)
    d %= n #5
    temp = [0]*n

    for i in range(n-d):
        temp[i]=arr[d+i]
    
    for i in range(d):
        temp[n-d+i]=arr[i]
    
    for i in range(n):
        arr[i]=temp[i]
    
    return arr


arr=[1,2,3,4,5,6]
d=3
print(rotateArr(arr,d))
