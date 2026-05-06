class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1_len = len(s1)
        # sorted_s1 = "".join(sorted(s1))
        # for i in range(len(s2)-s1_len+1):
        #     if sorted_s1 == "".join(sorted(s2[i:i+s1_len])):
        #         return True
        # return False
        s1_sorted = sorted(s1)
        s1_len = len(s1_sorted)
        # s1_chars = [*s1]
        # s1_chars = [c for c in s1 ]
        # for char in s1_chars:
        #     if char not in s2:
        #         return False

        # return True 
        for i in range(len(s1), len(s2)+1):
            x = sorted(s2[i-s1_len:i])
            if s1_sorted == x:
                return True
        return False




        

