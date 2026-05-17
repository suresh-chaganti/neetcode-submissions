class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        loop_cnt = len(nums) - k
        while loop_cnt > 0:
            heapq.heappop(nums)
            loop_cnt = loop_cnt -1 
            
        return heapq.heappop(nums)
        