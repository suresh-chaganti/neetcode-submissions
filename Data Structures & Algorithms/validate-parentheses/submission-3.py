class Solution:
    def isValid(self, s: str) -> bool:
        valid_para_dict = {'}':'{',')':'(',']':'['}
        stack_tmp = deque()
        for element in s:
            if element in valid_para_dict.values():
                stack_tmp.append(element)
            elif element in valid_para_dict:
                if not stack_tmp or stack_tmp.pop() != valid_para_dict.get(element):
                    return False
            else:
                return False
        
        return not stack_tmp


        