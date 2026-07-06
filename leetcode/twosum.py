
        
nums = [2,7,11,15,6,7,5,4,3,211,44]
target = 9
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        if(nums[j]+nums[i]==target):
            print(nums[j],nums[i])
        else:
            continue