# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def postorderDFS(root):
            if not root: return 0
            nonlocal ans
            lh = postorderDFS(root.left)
            rh = postorderDFS(root.right)
            ans = ans and abs(lh-rh) < 2
            return max(lh,rh) +1
        postorderDFS(root)
        return ans      
