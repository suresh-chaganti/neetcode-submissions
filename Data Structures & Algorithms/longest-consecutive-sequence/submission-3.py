class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = sorted(list(set(nums)))
        print(n)
        cnt = 1
        longest = cnt
        if len(nums) == 0:
            return 0
        first_num = n[0]
        for i in range(1,len(n)):
            if n[i] == n[i-1] + 1:
                cnt = cnt + 1
            elif cnt > longest:
                longest = cnt
                cnt = 1
            else:
                cnt = 1

        return max(longest, cnt)

        