class Solution:
    def simplifyPath(self, path: str) -> str:
        # We can use a stack to store the path
        # if .. is encountered pop 1 from stack
        # Tc: O(n) because split operation need O(n)
        # SP: O(n) n is number of character in path

        st = path.split('/')
        output = []

        for s in st:
            if s == '..':
                if len(output) > 0:
                    output.pop()
            elif s == '.' or s == '':
                continue
            else:
                output.append(s)

        return '/' + '/'.join(output)

