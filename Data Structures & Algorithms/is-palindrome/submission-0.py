class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(ss)
        print(ss[::-1])
        return ss.lower() == ss[::-1].lower()
        