class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        # If left child is None, we must go through right child
        if not root.left:
            return 1 + self.minDepth(root.right)

        # If right child is None, we must go through left child
        if not root.right:
            return 1 + self.minDepth(root.left)

        # If both children exist, take the minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().minDepth(root))

root2 = TreeNode(2)
root2.right = TreeNode(3)
root2.right.right = TreeNode(4)
root2.right.right.right = TreeNode(5)
root2.right.right.right.right = TreeNode(6)
print(Solution().minDepth(root2))