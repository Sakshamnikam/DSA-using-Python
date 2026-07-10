def maxConsecBits(arr):
    maxcount=0
    count=1

    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            count += 1
        else:
            maxcount=max(count,maxcount)
            count=1
    
    return max(maxcount,count)

ar=[1,0,0,0,1,1,0,1,0,1,1,1,1,0]
print(maxConsecBits(ar))