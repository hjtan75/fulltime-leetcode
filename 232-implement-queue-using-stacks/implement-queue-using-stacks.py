class MyQueue:
    # Make a FIFO queue with two queue
    # When push queue, push item into first stack
    # WHen peek or pop, if seconds stack is empty, transfer item from first to second stack
    # Otherwise, peek or pop from second stack
    # That way the order will be reverse
    # If both stack empty, then it's empty


    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while self.stack1:
                item = self.stack1.pop()
                self.stack2.append(item)
        return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) == 0:
            while self.stack1:
                item = self.stack1.pop()
                self.stack2.append(item)
        return self.stack2[-1]
        

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()