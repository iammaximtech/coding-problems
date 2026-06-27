class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        ans = []
        

        for k in range(len(nums)-1, 1, -1):
            if nums[k] < 0:
                break
            if k<len(nums)-1 and nums[k] == nums[k+1]:
                continue
            i = 0
            j = k-1
            while i<j:
                if nums[i]+nums[j] < - nums[k]:
                    i+=1
                elif nums[i]+nums[j] > - nums[k]:
                    j-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    i+=1
                    j-=1
                    while i<j and nums[i] == nums[i-1]:
                        i += 1
                    while i<j and nums[j] == nums[j+1]:
                        j -= 1
                
        return [list(each) for each in ans]
                 

