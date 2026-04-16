class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackk = []
        for token in tokens:
            if token in "+-*/":
                b = int(stackk.pop())
                a = int(stackk.pop())
                print(f'a is {a} and b is {b}')
                if token == '+':
                    val = a + b
                    print(val)
                    stackk.append(val)
                if token == '-':
                    val = a - b
                    print(val)
                    stackk.append(val)
                if token == '*':
                    val = a * b
                    print(val)
                    stackk.append(val)   
                if token == '/':
                    val = int(a / b)
                    print(val)
                    stackk.append(val)
            else:
                stackk.append(int(token))

        return stackk[0]