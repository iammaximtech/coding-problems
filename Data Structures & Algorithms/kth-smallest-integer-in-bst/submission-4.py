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
            nonlocal current, target, ans
            if not root or ans> -1: return
            inorder(root.left)
            current += 1
            if current == target:
                ans = root.val
                return
            inorder(root.right)

        inorder(root)
        return ans

            

        