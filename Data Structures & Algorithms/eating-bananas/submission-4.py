class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        bottom_hrs = 1
        top_hrs = max(piles)
        optimal_hrs = top_hrs
        while  bottom_hrs <= top_hrs:
            speed = (top_hrs + bottom_hrs) // 2
            totalTime = 0
            for pile in piles:
                totalTime = totalTime + math.ceil(pile/speed)
            
            if  totalTime <= h:
                optimal_hrs = speed
                top_hrs = speed - 1
            else:
                bottom_hrs = speed + 1
        return optimal_hrs




        
        