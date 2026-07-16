# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        dq = collections.deque()
        dq.append(root)
        while dq:
            n = len(dq)
            seen = False
            for i in range(n):
                curr= dq.popleft()
                if not seen:
                    ans.append(curr.val)
                    seen = True
                if curr.right:
                    dq.append(curr.right)
                if curr.left:
                    dq.append(curr.left)
        return ans