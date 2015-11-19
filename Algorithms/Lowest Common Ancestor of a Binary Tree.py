# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if p == root or q == root:
            return root
        L = self.lowestCommonAncestor(root.left, p, q)
        R = self.lowestCommonAncestor(root.right, p, q)
        if L and R:
            return root
        if L:
            return L
        else:
            return R