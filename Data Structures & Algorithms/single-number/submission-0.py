class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sett = set()
        for i in nums:
            if i in sett:
                sett.remove(i)
            else:
                sett.add(i)
        return sett.pop()
        
        
            
