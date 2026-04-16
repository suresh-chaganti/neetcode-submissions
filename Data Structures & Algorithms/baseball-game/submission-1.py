class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 1:
            operations[0]
        stack = []
        for i in range(len(operations)):
                
            if operations[i] == '+':
                stack.append(int(stack[-2])+int(stack[-1]))
            elif operations[i] == 'D':
                stack.append(2 * int(stack[-1]))
            elif operations[i] == 'C':
                stack.pop()
            else:
                stack.append(int(operations[i]))
        
        print(stack)
        return sum(stack)
        