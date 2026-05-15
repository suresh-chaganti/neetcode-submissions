class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            
            # if stones:
            #     if len(stones) > 1:
            #         while (len(stones) > 1):
            #             stones.sort()
            #             stone_left = stones.pop() - stones.pop()
            #             stones.append(stone_left)
            #         return stones[0]
            #     else:
            #         return stones[0]

            stones = [-s for s in stones]
            heapq.heapify(stones)

            while len(stones) > 1:
                first = heapq.heappop(stones)
                second = heapq.heappop(stones)
                if second > first:
                    heapq.heappush(stones, first - second)

            return abs(stones[0]) if stones else 0
            





        




        