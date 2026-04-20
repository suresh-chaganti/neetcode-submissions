class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0] * (max(nums)+1)
        print(arr)
        for num in nums:
            arr[num] = arr[num]+1

        i = 0
        for n in range(len(arr)):
            for j in range(arr[n]):
                nums[i] = n
                i += 1
        return nums 