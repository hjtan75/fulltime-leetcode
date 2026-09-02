class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.min = value
            self.stack.append(0)
        else:
            self.stack.append(value - self.min)
            if value < self.min:
                self.min = value

    def pop(self) -> None:
        pop_val = self.stack.pop()

        if pop_val < 0:
            self.min = self.min - pop_val

    def top(self) -> int:
        val = self.stack[-1]

        if val < 0:
            return self.min
        else:
            return self.min + val
            
    

    def getMin(self) -> int:
        return self.min
        
