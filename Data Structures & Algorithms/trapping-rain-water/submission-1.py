class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        prefixMax = [0]*len(height)
        suffixMax = [0]*len(height)
        leftMax = 0
        rightMax = 0

        for i in range(len(height)):
            if i-1 >= 0:
                leftMax = max(leftMax, height[i-1])
            prefixMax[i] = leftMax
        for j in range(len(height)-1, -1 ,-1):
            if j+1 < len(height):
                rightMax = max(rightMax, height[j+1])
            suffixMax[j] = rightMax
        for k in range(len(height)-1):
            ans += max(0,min(prefixMax[k], suffixMax[k]) - height[k])
        return ans





