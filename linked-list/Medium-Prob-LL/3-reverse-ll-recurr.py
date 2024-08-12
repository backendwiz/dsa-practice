class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def reverse_linked_list(self):
        self.head = self._reverse(self.head)

    def _reverse(self, head):
        if head is None or head.next is None:
            return head

        new_head = self._reverse(head.next)

        head.next.next = head  # Make the next node point to the current head
        head.next = None  # Break the link to avoid cycles

        return new_head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Create a doubly linked list from an array and reverse it
dllist = LinkedList()
arr = [1, 2, 3, 4, 5]
dllist.construct_dll_from_array(arr)

# Display the original doubly linked list
print("Original Doubly Linked List:")
dllist.display()

# Reverse the doubly linked list
dllist.reverse_linked_list()

# Display the reversed doubly linked list
print("\nReversed Doubly Linked List:")
dllist.display()
