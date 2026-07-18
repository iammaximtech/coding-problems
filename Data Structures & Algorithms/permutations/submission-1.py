class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def permutation(curr, i, picked):
            if len(curr) == len(nums):
                ans.append(curr.copy())
            for j in range(len(nums)):
                if not picked[j]:
                    picked[j]= True
                    curr.append(nums[j])
                    permutation(curr,j,picked)
                    curr.pop()
                    picked[j]=False
            

        permutation([], 0, [False]*len(nums))
        return ans