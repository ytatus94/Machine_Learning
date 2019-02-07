class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        if not root:
            return

        # swap two subtrees
        root.left, root.right = root.right, root.left

        # apply the same procedure to all the childern
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
