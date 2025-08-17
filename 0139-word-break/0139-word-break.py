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
        memory = [False] * (len(s) + 1)
        memory[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    memory[i] = memory[i + len(w)]
                if memory[i]:
                    break
        return memory[0]
