class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr = []
        ans = []

        def backtrackingInorder(i, nums, curr, ans):
            if i>=len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            backtrackingInorder(i+1,nums,curr,ans)
            curr.pop()
            backtrackingInorder(i+1,nums,curr,ans)
        backtrackingInorder(0,nums,curr,ans)
        return ans
