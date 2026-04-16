class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        sorted_s1 = "".join(sorted(s1))
        for i in range(len(s2)-s1_len+1):
            if sorted_s1 == "".join(sorted(s2[i:i+s1_len])):
                return True
        return False
        

