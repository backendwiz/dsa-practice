class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def middleNode(self, head):

#         slow, fast = head, head

#         while fast and fast.next:
#             slow, fast = slow.next, fast.next.next
#         return slow

#     # when want to use array use this method
#     # Create a linked list from an array
#     def createLinkedList(self, arr):
#         if not arr:
#             return None
#         head = ListNode(arr[0])
#         current = head
#         for i in range(1, len(arr)):
#             current.next = ListNode(arr[i])
#             current = current.next
#         return head


# arr = [1, 2, 3, 4, 5]
# ll = LinkedList()
# head = ll.createLinkedList(arr)

# middle = ll.middleNode(head)
# print(middle.val)


# or this


def middleNode(head):

    slow, fast = head, head

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    return slow


def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

middle = middleNode(head)
print(middle.val)
