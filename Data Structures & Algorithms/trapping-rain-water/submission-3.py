class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        size = len(height)
        if size == 0:
            return ans
        l, r = 0, size -1
        leftMax = height[l]
        rightMax = height[r]
        while l<r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -=1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        return ans