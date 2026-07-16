class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points or not k: return []
        if k>=len(points): return points
        distance = lambda x: x[0]**2 + x[1]**2

        def quickSelect(l,r):
            pivot = r
            left = l
            pivotDistance = distance(points[pivot])
            for i in range(l,r):
                if  distance(points[i])< pivotDistance:
                    points[left], points[i] = points[i], points[left]
                    left += 1
            points[left], points[r] = points[r], points[left]
            return left
        l, r = 0, len(points)-1
        pivot = len(points)+1
        while pivot!=k:
            pivot = quickSelect(l,r)
            if pivot < k:
                l = pivot +1
            else:
                r = pivot -1
        return points[:k]