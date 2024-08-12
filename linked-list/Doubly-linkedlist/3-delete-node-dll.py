class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def construct_dll_from_array(self, arr):
        if not arr:
            return
        self.head = Node(arr[0])
        current = self.head
        for data in arr[1:]:
            new_node = Node(data)
            current.next = new_node
            new_node.prev = current
            current = current.next

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        if not self.head.next:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def delete_at_end(self):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_at_position(self, position):
        if position <= 0 or not self.head:
            print("Invalid position or empty list.")
            return
        current = self.head
        if position == 1:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return
        current_position = 1
        while current_position < position and current:
            current = current.next
            current_position += 1
        if not current:
            print("Position out of bounds.")
            return
        prev_node = current.prev
        prev_node.next = current.next
        if current.next:
            current.next.prev = prev_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Create a doubly linked list from an array and perform deletions
dllist = DoublyLinkedList()
arr = [1, 2, 3, 4, 5]
dllist.construct_dll_from_array(arr)

# Display the doubly linked list
dllist.display()

# Delete node at the beginning
dllist.delete_at_beginning()

# Display the doubly linked list after deletion at the beginning
dllist.display()

# Delete node at the end
dllist.delete_at_end()

# Display the doubly linked list after deletion at the end
dllist.display()

# Delete node at position 2
dllist.delete_at_position(2)

# Display the doubly linked list after deletion at position 2
dllist.display()
