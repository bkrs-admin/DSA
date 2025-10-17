class MinStack:

    def __init__(self):
        self.data_stk = []
        self.min_stk = []

    def push(self, val: int) -> None:
        self.data_stk.append(val)

        if not self.min_stk:
            self.min_stk.append(val)
        else:
            prev_min = self.min_stk[-1]
            curr_min = min(prev_min, val)
            self.min_stk.append(curr_min)

    def pop(self) -> None:
        self.data_stk.pop()
        self.min_stk.pop()
        
    def top(self) -> int:
        return self.data_stk[-1]

    def getMin(self) -> int:
        return self.min_stk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()