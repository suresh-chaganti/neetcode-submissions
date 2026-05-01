class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res += [curr + [num] for curr in res]
        
        return res

        
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
        
#         def dfs(index, path):
#             res.append(path[:])  # add current subset
            
#             for i in range(index, len(nums)):
#                 path.append(nums[i])
#                 dfs(i + 1, path)
#                 path.pop()  # backtrack
        
#         dfs(0, [])
#         return res
