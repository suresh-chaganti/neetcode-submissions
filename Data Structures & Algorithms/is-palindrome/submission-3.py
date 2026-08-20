class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     ss = re.sub(r'[^a-zA-Z0-9]','', s)
    #     return ss.lower() == ss[::-1].lower()

    def isPalindrome(self, s: str) -> bool:

        ss = re.sub(r'[^a-zA-Z0-9]','',s)
        input = ss.lower()
        l,r = 0,len(ss)-1
        while l < r:
            if input[l] != input[r]:
                return False
            l = l+1
            r = r-1
        
        return True