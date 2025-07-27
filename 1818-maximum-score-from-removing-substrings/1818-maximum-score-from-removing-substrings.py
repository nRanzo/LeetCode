class Solution:
    # Use a stack to check for removable character pairs in a greedy way.
    # By iterating the string once for each pair ("ab" and "ba"), we process it efficiently.
    # The stack helps to look back one character and match pairs as they appear.
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def process(s, a, b, val):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    score += val
                else:
                    stack.append(ch)
            return ''.join(stack), score
        
        score = 0
        if x > y:
            s, gain = process(s, 'a', 'b', x)
            score += gain
            _, gain = process(s, 'b', 'a', y)
            score += gain
        else:
            s, gain = process(s, 'b', 'a', y)
            score += gain
            _, gain = process(s, 'a', 'b', x)
            score += gain
        return score