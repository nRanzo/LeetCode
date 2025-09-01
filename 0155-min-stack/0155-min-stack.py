class MinStack:
    def __init__(self):
        self.a = []
        self.min_values = deque()

    def push(self, val: int) -> None:
        self.a.append(val)
        if not self.min_values or val <= self.min_values[-1]:
            self.min_values.append(val)

    def pop(self) -> None:
        val = self.a.pop()
        if val == self.min_values[-1]:
            self.min_values.pop()

    def top(self) -> int:
        return self.a[-1]
        
    def getMin(self) -> int:
        return self.min_values[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()