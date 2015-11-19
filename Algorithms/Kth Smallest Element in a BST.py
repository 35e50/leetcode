# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def calNodes(self, root):
        if root == None:
            return 0
        return self.calNodes(root.left) + self.calNodes(root.right) + 1
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        nodes_left = self.calNodes(root.left)
        if nodes_left + 1 == k:
            return root.val
        elif nodes_left >= k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-nodes_left-1 )