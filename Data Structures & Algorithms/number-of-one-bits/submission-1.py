class Solution:
    def hammingWeight(self, n: int) -> int:
        counter  = 0
        # n = n & 0xffffffff
        while n:
            if n&1 == 1:
                counter +=1
            n = n >> 1
        return counter
        