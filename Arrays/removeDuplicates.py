def removeDuplicates(arr):
    n=len(arr)

    if n <= 1:
        return n

    idx=1

    for i in range(1,n):
        if arr[i] != arr[i-1]:
            arr[idx] = arr[i]
            idx += 1
    return idx

arr=[6,6,7,7,8,9,10]
newSize=removeDuplicates(arr) 
for i in range(newSize):
    print(arr[i])