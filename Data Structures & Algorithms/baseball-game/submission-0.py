class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 1:
            operations[0]
        resultant = []
        for i in range(len(operations)):
            if operations[i] not in ['+','D','C']:
                resultant.append(int(operations[i]))
            elif operations[i] == '+':
                resultant.append(int(resultant[-2])+int(resultant[-1]))
            elif operations[i] == 'D':
                resultant.append(2 * int(resultant[-1]))
            elif operations[i] == 'C':
                resultant.pop()
        
        print(resultant)
        return sum(resultant)
        