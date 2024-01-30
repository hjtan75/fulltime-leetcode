class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Use a stack to store the integers
        # When a expression is encountered, pop two integer from stack and evaluate the expression
        # After the evaluation insert the integer into the stack

        stack = []

        for token in tokens:
            if token == '+':
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(num_1 + num_2)

            elif token == '-':
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(num_1 - num_2)

            elif token == '*':
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(int(num_1 * num_2))

            elif token == '/':
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(int(num_1 / num_2))

            else:
                stack.append(int(token))

        return stack[0]