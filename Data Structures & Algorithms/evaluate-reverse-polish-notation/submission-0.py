class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(b + a)

                if token == '-':
                    stack.append(a - b)

                if token == '*':
                    stack.append(b * a)

                if token == '/':
                    stack.append(int(a / b))

            else:
                stack.append(int(token))

        return stack[0]
                

        