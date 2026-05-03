class Solution:
    def isValid(self, s: str) -> bool:
        ss = re.sub(r'[^\[\]\{\}\(\)]','', s)
        print(ss)
        while '()' in ss or '[]' in ss or '{}' in ss:
            ss = ss.replace('()','')
            ss = ss.replace('[]','')
            ss = ss.replace('{}','')
        return ss == ''