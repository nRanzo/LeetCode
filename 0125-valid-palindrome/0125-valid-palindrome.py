class Solution:
    def isPalindrome(self, s: str) -> bool: 
        clean = re.sub(r'[^a-z0-9]', '', s.lower())
        l, r = 0, len(clean) - 1
        while l < r:
            if not clean[l] == clean[r]:
                return False
            l += 1
            r -= 1
        return True