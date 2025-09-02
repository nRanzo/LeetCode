from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(curr: str, open_count: int, close_count: int):
            if open_count == n and close_count == n:
                res.append(curr)
                return

            if open_count < n:
                helper(curr + "(", open_count + 1, close_count)

            if close_count < open_count:
                helper(curr + ")", open_count, close_count + 1)

        helper("", 0, 0)
        return res