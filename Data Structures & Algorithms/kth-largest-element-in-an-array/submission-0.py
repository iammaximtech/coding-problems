class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k: return -1
        
        def quickSelect(l, r):
            pivot=nums[r]
            left = l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[left], nums[i] = nums[i], nums[left]
                    left+=1
            nums[left], nums[r]= nums[r], nums[left]
            return left
        
        l, r= 0, len(nums)-1
        k = len(nums)-k
        pivot = k+1 #non k number
        while pivot != k:
            pivot = quickSelect(l,r)
            if pivot < k:
                l = pivot+1
            else:
                r = pivot -1
        return nums[k]