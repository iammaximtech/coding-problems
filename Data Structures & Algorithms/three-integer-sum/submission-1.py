class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        ans = set()
        

        for k in range(len(nums)-1, 1, -1):
            i = 0
            j = k-1
            while i<j:
                if nums[i]+nums[j] < - nums[k]:
                    i+=1
                elif nums[i]+nums[j] > - nums[k]:
                    j-=1
                else:
                    ans.add((nums[i], nums[j], nums[k]))
                    i+=1
                    j-=1
                
        return [list(each) for each in ans]
                 

