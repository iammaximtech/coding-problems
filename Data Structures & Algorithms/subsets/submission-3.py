class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        ans = []

        def backtracking(i):
            if i>=len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            backtracking(i+1)
            curr.pop()
            backtracking(i+1)
        backtracking(0)
        return ans
