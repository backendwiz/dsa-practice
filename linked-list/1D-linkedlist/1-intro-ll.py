class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def constructLL(self, arr):
        # code here
        for value in arr:
            self.append(value)

    def display(self):
        """Print all nodes in the linked list."""
        current = self.head
        if not current:  # Check if the list is empty
            print("The list is empty.")
            return
        while current:
            if current.next:
                print(current.data, end=" ")
            else:
                print(current.data)
            current = current.next


ll = LinkedList()
arr = [1, 2, 3, 4, 5]
ll.constructLL(arr)
ll.display()
