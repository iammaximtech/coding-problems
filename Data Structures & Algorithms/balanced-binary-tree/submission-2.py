# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def postorderDFS(root):
            if not root: return 0

            lh = postorderDFS(root.left)
            if lh == -1: return -1

            rh = postorderDFS(root.right)
            if rh == -1: return -1

            balancedHeight = -1 if abs(lh-rh) > 1 else max(rh,lh)+1
            return balancedHeight

        ans = postorderDFS(root) != -1
        return ans      
