# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDm = 0
        self.postOrderDFS(root)
        return self.maxDm

    def postOrderDFS(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        lheight = self.postOrderDFS(root.left)
        rheight = self.postOrderDFS(root.right)
        self.maxDm = max(self.maxDm, lheight+rheight)
        return 1 + max(lheight, rheight)