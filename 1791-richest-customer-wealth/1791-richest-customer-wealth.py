class Solution:
    def maximumWealth(self, accounts):
        mW = 0
        for i in range(len(accounts)):
            tW = sum(accounts[i])
            mW = max(mW, tW)
        return mW