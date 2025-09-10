class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            tot = 0
            for p in piles:
                tot += math.ceil(p / k)
            if tot <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
            
        return res