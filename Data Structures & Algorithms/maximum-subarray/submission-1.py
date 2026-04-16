class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = nums[0]
        for i in range(len(nums)):
            cumSum = 0
            for j in range(i, len(nums)):
                cumSum = cumSum + nums[j]
                max_sum = max(max_sum, cumSum)
        
        return max_sum
        