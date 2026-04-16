class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) > 1:
            left, right = nums[0], nums[-1]
            if target >= left: 
                for i in range(len(nums)):
                    if nums[i] == target:
                        return i
                    if nums[i] > target:
                        return -1
            if target < left: 
                for i in range(len(nums)-1, -1, -1):
                    if nums[i] == target:
                        return i
                    if nums[i] < target:
                        return -1
        return -1
            