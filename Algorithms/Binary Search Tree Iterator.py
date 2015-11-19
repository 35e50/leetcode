# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.tree = []
        self.inOrderTraverse(root)
        self.idx = -1
        self.size = len(self.tree)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        self.idx += 1
        return self.idx < self.size

    # @return an integer, the next smallest number
    def next(self):
        return self.tree[self.idx]
    
    def inOrderTraverse(self, root):
        if root is None:
            return
        self.inOrderTraverse(root.left)
        self.tree.append(root.val)
        self.inOrderTraverse(root.right)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())