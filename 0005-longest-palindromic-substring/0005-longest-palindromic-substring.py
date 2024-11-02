class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        max_len = 1
        max_str = s[0]

        # Transform the string to handle both even and odd-length palindromes
        # by inserting '#' between characters and at the beginning and end
        s = '#' + '#'.join(s) + '#'

        # list to store the length of the palindrome radius at each character
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0

        for i in range(len(s)):
            # If i is within the current right boundary, set dp[i] to the minimum radius
            # either by mirroring the radius from the left side or by reaching the boundary
            if i < right:
                dp[i] = min(right - i, dp[2 * center - i])
            
            # Expand around the current center i, increasing the palindrome radius as long as characters match
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            
            # Update the center and right boundary if the expanded palindrome goes beyond the current boundary
            if i+dp[i] > right:
                center = i
                right = i + dp[i]
            if dp[i] > max_len:
                max_len = dp[i]
                max_str = s[i-dp[i]:i+dp[i]+1].replace('#', '')
        return max_str

