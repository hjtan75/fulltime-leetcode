class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in range(len(tokens)):
            if tokens[i].isnumeric() or (tokens[i][0] == '-' and len(tokens[i]) > 1):
                stack.append(int(tokens[i]))
                
            elif tokens[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
                
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
                
            elif tokens[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
                
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
                
                
        return stack[0]