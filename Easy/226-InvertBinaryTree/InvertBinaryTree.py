# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        left_subtree = root.left
        right_subtree = root.right
        root.left = self.invertTree(right_subtree)
        root.right = self.invertTree(left_subtree)
        return root

    # From geeksforgeeks.org/level-order-tree-traversal
    def height(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            # Compute the height of each subtree
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            return max(left_height + 1, right_height + 1)

    def printCurrentLevel(self, root: TreeNode, level: int):
        if root is None:
            return
        if level == 1:
            print(root.val, end=" ")
        elif level > 1:
            self.printCurrentLevel(root.left, level - 1)
            self.printCurrentLevel(root.right, level - 1)

    def printLevelOrder(self, root: TreeNode):
        h = self.height(root)
        for i in range(1, h+1):
            self.printCurrentLevel(root, i)


if __name__ == "__main__":
    solution = Solution()
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node6 = TreeNode(6)
    node9 = TreeNode(9)
    node7 = TreeNode(7, node6, node9)
    node4 = TreeNode(4, node2, node7)
    inverted_root = solution.invertTree(node4)
    solution.printLevelOrder(inverted_root)