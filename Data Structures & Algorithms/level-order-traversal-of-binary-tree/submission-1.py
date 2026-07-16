# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        dq = collections.deque()
        dq.append(root)
        n = len(dq)
        while dq:
            curr = []
            n = len(dq)
            for i in range(n):
                last = dq.popleft()
                if last.left: 
                    dq.append(last.left)
                if last.right:
                    dq.append(last.right)
                curr.append(last.val)
            ans.append(curr)
        return ans

            
        