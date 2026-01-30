class Solution:
    def Linear_Searching(self,nums,target):
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1
print(Solution().Linear_Searching([9,8,4,5,2,1],8))