class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []

        def combinationSumHelper(i, curr, total):
            if total == target:
                ans.append(curr.copy())
                return
            if i>len(nums) or total>target:
                return
            for j in range(i, len(nums)):
                if nums[j]+total>target:
                    return
                curr.append(nums[j])
                combinationSumHelper(j,curr,total+nums[j])
                curr.pop()
                
        combinationSumHelper(0,[],0)
        return ans
