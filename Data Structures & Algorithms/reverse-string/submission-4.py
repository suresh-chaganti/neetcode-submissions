class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # char = s
        # left,right = 0, len(s)-1
        # while left < right:
        #     char[left],char[right] = char[right],char[left]
        #     left = left+1
        #     right = right-1 
        # s = "".join(char)
        
        s[:] = s[::-1]
        