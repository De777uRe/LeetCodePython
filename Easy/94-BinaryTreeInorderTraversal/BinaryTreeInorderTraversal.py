from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        retval = []
        if root:
            retval = self.inorderTraversal(root.left)
            retval.append(root.val)
            retval += self.inorderTraversal(root.right)
        return retval


if __name__ == "__main__":
    solution = Solution()
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)
    node4 = TreeNode(4, node2, node7)
    traversal_result = solution.inorderTraversal(node4)
    print(traversal_result)
