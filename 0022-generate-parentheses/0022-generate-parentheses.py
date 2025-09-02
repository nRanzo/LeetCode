class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = deque()

        def helper(num_open: int, num_close: int):
            if num_open == n and num_close == n:
                res.append("".join(stack))
                return

            if num_open < n:
                stack.append('(')   # goes down in associated tree
                helper(num_open + 1, num_close)
                stack.pop()         # go up in associated tree
            
            if num_close < num_open:
                stack.append(')')
                helper(num_open, num_close + 1)
                stack.pop()

        helper(0, 0)
        return res