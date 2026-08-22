class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_val = {}
        for index, num in enumerate(numbers):
            second_num = target - num
            if second_num in dict_val:
                return [dict_val[second_num], index+1]
            else:
                dict_val[num] = index+1

        return list()
        

        