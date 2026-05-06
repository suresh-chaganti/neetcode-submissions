# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1_len = len(s1)
        # sorted_s1 = "".join(sorted(s1))
        # for i in range(len(s2)-s1_len+1):
        #     if sorted_s1 == "".join(sorted(s2[i:i+s1_len])):
        #         return True
        # return False
        # s1_sorted = sorted(s1)
        # s1_len = len(s1_sorted)
        # s1_chars = [*s1]
        # s1_chars = [c for c in s1 ]
        # for char in s1_chars:
        #     if char not in s2:
        #         return False

        # return True 
        # for i in range(len(s1), len(s2)+1):
        #     x = sorted(s2[i-s1_len:i])
        #     if s1_sorted == x:
        #         return True
        # return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        s2_count = [0] * 26

        # Fill initial counts for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Matches tracks how many characters (0-25) have the same frequency
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1

        # Slide the window across s2
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Character entering from the right
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            # Character leaving from the left
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            l += 1

        return matches == 26


        

