from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucketFreq= [[] for i in range (len(nums)+1)]
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        for key, val in freq.items():
            bucketFreq[val].append(key)
        ans = []
        for i in range(len(bucketFreq)-1, 0, -1):
            for num in bucketFreq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans  
        return ans      

        