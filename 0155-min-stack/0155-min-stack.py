class MinStack:

    def __init__(self):
        self.min_val = []
        self.stack = []

    def push(self, val: int) -> None:
        if not self.min_val or val <= self.min_val[-1]:
            self.min_val.append(val)
        self.stack.append(val)
        return

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_val[-1]:
            self.min_val.pop()
        return
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()