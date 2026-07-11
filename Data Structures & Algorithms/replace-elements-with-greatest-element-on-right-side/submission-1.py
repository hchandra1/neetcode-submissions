class Solution:
    def replaceElements(self, nums: List[int]) -> List[int]:
        maxn = -1
        for i in range(len(nums)-1,-1,-1):
            nums[i],maxn = maxn, max(nums[i],maxn)
        return nums
       
            
           

        