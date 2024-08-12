class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def is_empty(self):
        return self.start is None

    def peek(self):
        if self.is_empty():
            return -1  # Queue is empty
        return self.start.data

    def enqueue(self, data):
        new = Node(data)
        if self.end is None:
            self.start = self.end = new
            return
        self.end.next = new
        self.end = new

    def dequeue(self):
        if self.is_empty():
            return -1
        dequeued_data = self.start.data
        self.start = self.start.next
        if self.start is None:
            self.end = None
        return dequeued_data


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(1)

    # print(queue.dequeue())
    # print(queue.dequeue())  # Outputs: 1
    print(queue.dequeue())  # Outputs: 1
    print(queue.peek())
