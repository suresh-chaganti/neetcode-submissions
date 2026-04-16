class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        length = len(nums)
        # Solution 1
        # ans = []

        # for i in range(2):
        #     for num in nums:
        #         ans.append(num)

        # print(ans)
        # return ans 

        # Solution 2 

        # ans = [0] * 2 * length
        # for index, num in enumerate(nums):
        #     ans[index] = ans[index+length] = num

        # print(ans)
        # return ans 

        # Solution 3
        
        return nums + nums
        

        