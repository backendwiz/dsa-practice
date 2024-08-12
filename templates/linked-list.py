class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Append a node with the specified data to the end of the list."""
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def display(self):
        """Display the elements of the linked list."""
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


if __name__ == "__main__":
    ll = LinkedList()

    # Example usage
    for i in range(1, 6):
        ll.append(i)

    ll.display()  # Display the linked list
