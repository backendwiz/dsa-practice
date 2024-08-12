class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)

        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if __name__ == "__main__":
    # Create a MinStack instance
    min_stack = MinStack()

    # Push values onto the stack
    min_stack.push(3)
    min_stack.push(5)
    print(min_stack.getMin())  # Should print 3

    min_stack.push(2)
    min_stack.push(1)
    print(min_stack.getMin())  # Should print 1

    min_stack.pop()
    print(min_stack.getMin())  # Should print 2

    min_stack.pop()
    print(min_stack.top())  # Should print 5
    print(min_stack.getMin())  # Should print 3
