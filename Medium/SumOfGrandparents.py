class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        pass


def build_tree(node_list):
    if len(node_list) > 0:
        root = TreeNode(node_list[0])


if __name__ == "__main__":
    solution = Solution()
    root = [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5]