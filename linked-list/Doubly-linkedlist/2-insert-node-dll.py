class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert_at_position(self, data, position):
        if position <= 0:
            print("Position must be a positive integer.")
            return
        if position == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        current_position = 1
        while current_position < position - 1 and current.next:
            current = current.next
            current_position += 1
        if current_position == position - 1:
            new_node.next = current.next
            new_node.prev = current
            if current.next:
                current.next.prev = new_node
            current.next = new_node
        else:
            print("Position out of bounds. Node added at the end.")
            self.insert_at_end(data)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Create a doubly linked list and perform insertions
dllist = DoublyLinkedList()
dllist.insert_at_beginning(3)
dllist.insert_at_beginning(2)
dllist.insert_at_beginning(1)
dllist.insert_at_end(4)
dllist.insert_at_end(5)
dllist.display()
dllist.insert_at_position(99, 3)

# Display the doubly linked list
dllist.display()
