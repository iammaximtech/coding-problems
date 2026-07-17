class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        ans = []

        def backtrackingInorder(i):
            if i>=len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            backtrackingInorder(i+1)
            curr.pop()
            backtrackingInorder(i+1)
        backtrackingInorder(0)
        return ans
