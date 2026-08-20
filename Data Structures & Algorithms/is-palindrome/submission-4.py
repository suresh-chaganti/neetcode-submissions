class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     ss = re.sub(r'[^a-zA-Z0-9]','', s)
    #     return ss.lower() == ss[::-1].lower()

    def isPalindrome(self, s: str) -> bool:

        ss = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        
        l,r = 0,len(ss)-1
        while l < r:
            if ss[l] != ss[r]:
                return False
            l = l+1
            r = r-1
        
        return True