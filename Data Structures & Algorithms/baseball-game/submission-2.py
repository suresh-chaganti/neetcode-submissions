class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 1:
            operations[0]
        stack = []
        for op in operations:
                
            if op == '+':
                stack.append(int(stack[-2])+int(stack[-1]))
            elif op == 'D':
                stack.append(2 * int(stack[-1]))
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        print(stack)
        return sum(stack)
        