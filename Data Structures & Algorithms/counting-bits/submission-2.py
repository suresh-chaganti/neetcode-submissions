class Solution:
    def countBits(self, n: int) -> List[int]:
        lst = []
        for i in range(n+1):
            bin_num = i & 0xffffffff
            cnt = 0
            while bin_num:
                cnt += bin_num % 2
                bin_num = bin_num >> 1
            lst.append(cnt)
        return lst


        