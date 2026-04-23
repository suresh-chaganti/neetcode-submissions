class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bottom_hrs = 1
        top_hrs = max(piles)
        optimal_hrs = bottom_hrs
        final_hrs = 0
        while bottom_hrs <= top_hrs:
            optimal_hrs = 0
            mid_hrs = (top_hrs + bottom_hrs) // 2
            for pile in piles:
                optimal_hrs = optimal_hrs + math.ceil(pile/mid_hrs)

            if optimal_hrs <= h:
                top_hrs = mid_hrs - 1
                final_hrs = mid_hrs
            else:
                bottom_hrs = mid_hrs + 1  
                
        return final_hrs