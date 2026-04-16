class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub(r'[^a-zA-Z0-9]','', s)
        return ss.lower() == ss[::-1].lower()