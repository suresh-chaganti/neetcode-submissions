class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            second_num = target - num
            if second_num in dic:
                return [dic[second_num], index]
            else:
                dic[num] = index
