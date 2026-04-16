class Solution:
    def validPalindrome(self, s: str) -> bool:

        left, right = 0, len(s)-1
        while left < right:
            if s[left] == s[right]:
                left = left +1
                right = right - 1
            else:
                skip_l = s[left+1:right+1]
                skip_r = s[left:right]
                return skip_l.lower() == skip_l[::-1].lower() or skip_r.lower() == skip_r[::-1].lower() 

        return True 




                
            
        