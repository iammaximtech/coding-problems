# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDm = 0

        def postOrderDFS(root):
            nonlocal maxDm
            if not root: return 0
            
            lheight = postOrderDFS(root.left)
            rheight = postOrderDFS(root.right)
            maxDm = max(maxDm, lheight+rheight)
            return 1 + max(lheight, rheight)
        
        postOrderDFS(root)
        return maxDm