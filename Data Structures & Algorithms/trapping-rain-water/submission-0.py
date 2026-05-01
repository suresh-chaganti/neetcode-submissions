class Solution:
    def trap(self, height: List[int]) -> int:
        # Need at least 3 bars to trap water
        if len(height) < 3:
            return 0

        maxMap = defaultdict(list)

        # Store max left for each index
        currMax = -float("inf")
        for i in range(1, len(height) - 1):
            currMax = max(currMax, height[i - 1])
            maxMap[i].append(currMax)

        # Store max right for each index
        currMax = -float("inf")
        for i in range(len(height) - 2, 0, -1):
            currMax = max(currMax, height[i + 1])
            maxMap[i].append(currMax)

        # Calculate trapped water at each index
        res = 0
        for i in range(1, len(height) - 1):
            res += max(0, min(maxMap[i]) - height[i])

        return res