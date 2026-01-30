class Solution:
    def Binary_Searching(self,nums,target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
print(Solution().Binary_Searching([-1,0,8,9,10,11],-1))