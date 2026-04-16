class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ana = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            print(sorted_word)
            if sorted_word in dict_ana:
                dict_ana[sorted_word].append(word)
            else:
                dict_ana[sorted_word] = [word]
        
        return list(dict_ana.values())
        