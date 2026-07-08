def second_largest(arr):
    n=len(arr)

    largest=-1
    sec_largest=-1

    for i in range(n):
        if (arr[i]>largest):
            sec_largest=largest
            largest=arr[i]

        elif(arr[i]<largest and arr[i]>sec_largest):
            sec_largest=arr[i]
            
    
    return sec_largest        
          
    

arr=[12,35,1,10,10,34,1]
print(arr)
print('2nd Largest Element is:',second_largest(arr))