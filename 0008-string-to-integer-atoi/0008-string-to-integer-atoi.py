class Solution:
    def myAtoi(self, s: str) -> int:
        # linear time because the each operation is perfomed
        # due to the inner or outer loop, not both
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i, n = 0, len(s)
        res = 0
        neg = False

        # skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # handle optional sign
        if i < n and s[i] in ('-', '+'):
            neg = s[i] == '-'
            i += 1

        # parse digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # clamp before overflow
            if res > (INT_MAX - digit) // 10:
                return INT_MIN if neg else INT_MAX

            res = res * 10 + digit
            i += 1

        return -res if neg else res