class Node:

    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1


def display(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next


def append(data):
    if not head:
        head = Node(data)
    else:
        current = head
        while current.next:
            current = current.next
        current.next = Node(data)


# Function to insert a node at the end of the linked list.
def insertAtEnd(head, val):

    # insert at head
    # temp = Node(val, head)
    # return temp

    # insert at end
    if head is None:
        return Node(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = Node(val)
    return head


if __name__ == "__main__":
    # Sample array and value for insertion
    arr = [12, 8, 5, 7]
    val = 100

    # Creating a linked list with initial elements from the array
    head = Node(arr[0])
    curr = head
    for data in arr[1:]:
        curr.next = Node(data)
        curr = curr.next

    # Inserting a new node at the head of the linked list
    head = insertAtEnd(head, val)

    # Printing the linked list
    display(head)
