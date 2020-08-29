# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        ret = ""
        while curr != None:
            ret += str(curr.val) + "->"
            curr = curr.next
        return ret

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            if l1 is not None:
                return l1
            if l2 is not None:
                return l2
            return None

        l1_head = l1
        l2_head = l2
        ret_list = None
        curr_ret = None
        while l1_head is not None or l2_head is not None:
            new_node = ListNode()
            copy_node = ListNode()
            if l1_head.val < l2_head.val:
                new_node.val = l1_head.val
                copy_node.val = l2_head.val
            elif l1_head.val > l2_head.val:
                new_node.val = l2_head.val
                copy_node.val = l1_head.val
            else:
                new_node.val = l1_head.val
                copy_node.val = l1_head.val

            if curr_ret is None:
                curr_ret = new_node
                curr_ret.next = copy_node
                ret_list = curr_ret
                curr_ret = copy_node
            else:
                curr_ret.next = new_node
                curr_ret = new_node
                curr_ret.next = copy_node
                curr_ret = copy_node

            l1_head = l1_head.next
            l2_head = l2_head.next

        return ret_list



def test_1():
    solution = Solution()

    list1_tail = ListNode(4)
    list1_2 = ListNode(2, list1_tail)
    list1_head = ListNode(1, list1_2)

    list2_tail = ListNode(4)
    list2_2 = ListNode(3, list1_tail)
    list2_head = ListNode(1, list2_2)

    print("Expected: 1->1->2->3->4->4 ")
    print("Actual: " + str(solution.mergeTwoLists(list1_head, list2_head)))

if __name__ == "__main__":
    test_1()
