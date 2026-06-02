class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        small = -1
        big = -1
        for i, n in enumerate(nums):
                for j, m in enumerate(nums):
                    if i!=j and n+m == target:
                        small = i if i < j else j
                        big = j if j> i else i
                        break
        return [small, big]

        