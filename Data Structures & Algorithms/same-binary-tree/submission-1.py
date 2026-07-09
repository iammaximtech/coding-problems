# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
            def preOrderDFS(a,b):
                if not a or not b:
                    if not a and not b: return True
                    else: return False
                if a.val != b.val: return False
                left = preOrderDFS(a.left,b.left)
                if not left: return False
                right = preOrderDFS(a.right,b.right)
                if not right: return False
                return True

            return preOrderDFS(p,q)
                