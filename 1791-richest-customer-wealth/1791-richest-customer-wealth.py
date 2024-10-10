class Solution(object):
    def maximumWealth(self, accounts):
        sums = [sum(i) for i in accounts]
        return max(sums)