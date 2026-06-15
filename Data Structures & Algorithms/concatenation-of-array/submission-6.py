class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]* (2*len(nums))
        left =0
        right = len(nums)
        while right < 2*len(nums):
            ans[left]= ans[right] = nums[left]
            left+=1
            right+=1
        return ans