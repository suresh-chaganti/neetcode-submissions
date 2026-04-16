class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) > 1:
            start = nums[0]
            end = nums[-1]
            if start < end:
                return start
            
            for i in range(len(nums)-1, -1, -1):
                if nums[i] <= end:
                    end = nums[i]
                else:
                    break 
            
            return end
        