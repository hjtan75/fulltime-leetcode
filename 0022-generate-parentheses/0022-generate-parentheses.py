class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def addParent(numLeft, numRight, numMax, oldString):
            if numLeft == numMax:
                if numRight == numMax:
                    res.append(oldString)
                    return
                else:
                    # newRight = numRight + 1
                    addParent(numLeft, numRight + 1, numMax, str(oldString) + ')')
            else:
                # newLeft = numLeft + 1
                addParent(numLeft + 1, numRight, numMax, str(oldString) + '(')
                if numLeft > numRight:
                    # newRight = numRight + 1
                    addParent(numLeft, numRight + 1, numMax, str(oldString) + ')')
            return

        
        if n == 0:
            return []
        
        
        addParent(1, 0, n, '(')
        

        return res
    