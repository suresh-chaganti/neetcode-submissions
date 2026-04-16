class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic_nums = {}
        top_k_nums = []    
    
        for num in nums:
            if num in dic_nums:
                dic_nums[num] = dic_nums[num] + 1
            else:
                dic_nums[num] = 1
        
        return sorted(dic_nums, key=dic_nums.get, reverse=True)[:k]
         
        