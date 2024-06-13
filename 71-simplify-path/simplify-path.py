class Solution:
    def simplifyPath(self, path: str) -> str:
        # We can use a stack to store the path
        # if .. is encountered pop 1 from stack
        # Tc: O(n) because split operation need O(n)
        # SP: O(n) n is number of character in path

        dir_stack, output = [], []
        for c in path:
            if c == '/':
                if len(dir_stack) > 0:
                    d = ''.join(dir_stack)
                    dir_stack = []
                    if '.' == d:
                        continue
                    elif '..' == d:
                        if len(output) > 0:
                            output.pop()
                    else:
                        output.append(d)
            else:
                dir_stack.append(c)

        if len(dir_stack) > 0:
            d = ''.join(dir_stack)
            if '.' == d:
                pass
            elif '..' == d:
                if len(output) > 0:
                    output.pop()
            else:
                output.append(d)


        return '/' + '/'.join(output)

