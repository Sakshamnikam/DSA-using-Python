class Solution(object):
    def twoSum(self, nums, target):
        
        ls=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if(nums[i]+nums[j]==target):
                    ls=[i,j]
        return ls

        
        
        
s=Solution()
nums=[3,3]
target=6
ans=s.twoSum(nums,target)
print(ans)
