class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new = Node(data)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.is_empty():
            return -1
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.is_empty():
            return -1  # Stack is empty
        return self.top.data


# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())  # Outputs: 2
    print(stack.pop())
    print(stack.peek())  # Outputs: 1
