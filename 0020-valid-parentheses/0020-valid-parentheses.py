class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        mapp = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in mapp.values():     # values are ( [ {
                q.append(ch)
            elif ch in mapp:            # keys are ) ] }
                if not q or q[-1] != mapp[ch]:
                    return False
                q.pop()
            else:
                return False
        return not q