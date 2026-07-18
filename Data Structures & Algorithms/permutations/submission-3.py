class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def permutation(curr, picked):
            if len(curr) == len(nums):
                ans.append(curr.copy())
            for j in range(len(nums)):
                if not picked[j]:
                    picked[j]= True
                    curr.append(nums[j])
                    permutation(curr,picked)
                    curr.pop()
                    picked[j]=False
            

        permutation([], [False]*len(nums))
        return ans