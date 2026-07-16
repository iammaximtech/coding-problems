# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        target = k
        current = 0
        ans = -1
        
        def inorder(root):
            if not root: return
            nonlocal current
            nonlocal target
            nonlocal ans
            inorder(root.left)
            current += 1
            if current == target:
                ans = root.val
                return
            inorder(root.right)

        inorder(root)
        return ans

            

        