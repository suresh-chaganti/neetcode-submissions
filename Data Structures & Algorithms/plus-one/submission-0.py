class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = "".join([str(x) for x in digits])
        k = int(s)+1
        return [int(d) for d in (str(k))]