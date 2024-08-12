class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(data)

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Loop detected
        return False  # No loop detected


if __name__ == "__main__":
    ll = LinkedList()

    # Append data to the linked list
    arr = [1, 2, 3, 4, 5]
    for item in arr:
        ll.append(item)

    # Create a loop for testing
    ll.head.next.next.next.next.next = (
        ll.head.next
    )  # Creating a cycle back to the second node

    # Display the linked list (may enter an infinite loop due to the cycle)
    # ll.display()  # Uncommenting this will result in an infinite loop

    # Check for cycle
    has_cycle = ll.detect_cycle()
    print("Cycle detected:", has_cycle)
