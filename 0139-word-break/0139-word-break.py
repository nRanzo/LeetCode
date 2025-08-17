class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not self.greedy(s, wordDict):
            return self.dp(s, wordDict)
        return True

    # may cause false negative, but never false positive
    def greedy(self, s: str, wordDict: List[str]) -> bool:
        l, r = 0, 1
        while r <= len(s):
            tmp = s[l:r]
            if tmp in wordDict:
                l = r
            r += 1
        if len(tmp) != 0 and not tmp in wordDict:
            return False
        return True
    
    # never false pos or false neg, costs more
    def dp(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        if not wordSet: 
            return False
        minL = min(map(len, wordSet))
        maxL = max(map(len, wordSet))
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            if not dp[i]: 
                continue
            # only valid length
            for L in range(minL, maxL+1):
                j = i + L
                if j <= n and s[i:j] in wordSet:
                    dp[j] = True
                    if j == n:    # early exit
                        return True
        return dp[n]