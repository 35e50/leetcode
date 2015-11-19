# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return result
        q = []
        q.append(root)
        q.append(None)
        
        while q:
            node = q.pop(0)
            if node == None:
                if q == []:
                    break
                else:
                    q.append(None)
            else:
                if q[0] == None:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result