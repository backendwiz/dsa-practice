class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def linked_list(self, head, key):

        temp = self.head
        while temp is not None:
            if temp.data == key:
                return True
            temp = temp.next
        return False


if __name__ == "__main__":
    arr = [2, 4, 8, 7]
    key = 5
    # Create a linked list
    ll = LinkedList()
    for item in arr:
        ll.append(item)

    # Print the length of the linked list
    print(ll.linked_list(arr, key))
