class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            tot = reduce(lambda acc, p: acc + math.ceil(p / k), piles, 0)
            if tot <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            
        return res