class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        node_head = ListNode()
        if list1 and list2:
            if list1.val < list2.val:
                node_head = list1
                node_tail = self.mergeTwoLists(list1.next, list2)
            else:
                node_head = list2
                node_tail = self.mergeTwoLists(list1, list2.next)
            node_head.next = node_tail
            return node_head
        else:
            return list2 if not list1 else list1
    
def print_linked_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(4)


list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


list3 = Solution().mergeTwoLists(list1, list2)
print_linked_list(list3)