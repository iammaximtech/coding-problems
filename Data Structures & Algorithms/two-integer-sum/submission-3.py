class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        small = -1
        big = -1
        map = {}
        for i, n1 in enumerate(nums):
            n2=target-n1
            if n2 in map and map.get(n2)!=i:
                j = map.get(n2)
                small = i if i<j else j
                big = i if i>j else j
                break
            else:
                 map[n1] = i 
        return [small, big]

        