class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def combinationSumHelper(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return 
            if total>target or i>=len(nums):
                return
               
            curr.append(nums[i])
            combinationSumHelper(i+1, curr, total+nums[i])
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                    i+=1
            combinationSumHelper(i+1, curr, total)
        combinationSumHelper(0, [], 0)
        return ans
        