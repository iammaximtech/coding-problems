class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n1 in enumerate(nums):
            n2=target-n1
            if n2 in seen:
                return [seen[n2], i]
            else:
                 seen[n1] = i 

        