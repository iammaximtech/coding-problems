class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def combinationSumHelper(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            for j in range(i, len(nums)):
                if nums[j]+total>target:
                    return
                if j>i and nums[j]==nums[j-1]:
                    continue
                curr.append(nums[j])
                combinationSumHelper(j+1, curr, total+nums[j])
                curr.pop()
        combinationSumHelper(0, [], 0)
        return ans
        