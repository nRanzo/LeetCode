class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_tmp = sx = dx = 0
        seen = {}
        for idx, c in enumerate(s):
            if c in seen:
                if dx - sx > max_tmp:
                    max_tmp = dx - sx
                if sx < seen[c] + 1:
                    sx = seen[c] + 1
            seen[c] = idx
            dx = idx + 1
        if dx - sx > max_tmp:
            max_tmp = dx - sx
        return max_tmp
