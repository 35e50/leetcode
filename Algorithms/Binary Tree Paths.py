# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.result = []
        if root == None:
            return []
        def dfs(root, path):
            if root.left == None and root.right == None:
                self.result.append(path)
            if root.left:
                dfs(root.left, path+"->"+str(root.left.val))
            if root.right:
                dfs(root.right, path+"->"+str(root.right.val))
        dfs(root, str(root.val))
        return self.result