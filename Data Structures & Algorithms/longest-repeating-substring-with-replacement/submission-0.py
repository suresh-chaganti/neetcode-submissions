class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_count = defaultdict(int)
        max_char = 0
        sol = 0
        while r < len(s):
            char_count[s[r]] += 1

            max_char = max(char_count[s[r]], max_char)
            replacements = r - l + 1 - max_char
            if replacements > k:
                char_count[s[l]] -= 1
                l += 1
            
            sol = max(r-l+1, sol)
            r += 1
        return sol
            

        