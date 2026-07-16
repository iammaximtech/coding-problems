# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        top = float("-inf")
        if not root: return 0
        

        def dfs(root, top):
            if not root: return 0
            ans = 0
            
            if root.val>=top:
                ans += 1
                top = root.val
            ans += dfs(root.left, top) 
            ans += dfs(root.right, top)
            return ans
        ans = dfs(root,top)
        return ans
        
        