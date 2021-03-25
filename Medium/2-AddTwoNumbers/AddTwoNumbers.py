# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_head = result
        l1_head = l1
        l2_head = l2
        while l1_head is not None or l2_head is not None:
            if l1_head is not None:
                result_head.val += l1_head.val
                l1_head = l1_head.next
            if l2_head is not None:
                result_head.val += l2_head.val
                l2_head = l2_head.next
            if result_head.val > 9:
                result_head.val %= 10
                result_head.next = ListNode(1)
            else:
                if l1_head is not None or l2_head is not None:
                    result_head.next = ListNode(0)
            result_head = result_head.next
        return result


if __name__ == "__main__":
    l1_1 = ListNode(1)
    l1_2 = ListNode(8)
    l1_1.next = l1_2
    # l1_3 = ListNode(3)
    # l1_2.next = l1_3

    l2_1 = ListNode(0)
    # l2_2 = ListNode(6)
    # l2_1.next = l2_2
    # l2_3 = ListNode(4)
    # l2_2.next = l2_3

    solution = Solution()
    result = solution.addTwoNumbers(l1_1, l2_1)
    while result is not None:
        print(result.val, end=' ')
        result = result.next
