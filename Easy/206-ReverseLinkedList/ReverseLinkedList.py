# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr is not None:
            temp_curr = curr.next
            curr.next = prev
            prev = curr
            curr = temp_curr
        return prev

    def printList(self, head: ListNode):
        curr = head
        while curr is not None:
            print(f'{curr.val} ->', end=' ')
            curr = curr.next
        print('None')


if __name__ == "__main__":
    solution = Solution()
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    reversed_head = solution.reverseList(node1)
    solution.printList(reversed_head)
