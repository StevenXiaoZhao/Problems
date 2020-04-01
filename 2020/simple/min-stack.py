class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
    data = []
    min_val = int('inf')
    def push(self, x: int) -> None:
        self.data.append(x)
        if x < self.min_val:
            self.min_val = x
    def pop(self) -> None:
        if len(self.data) >0:
            self.data.pop()
            self.min_val = min(self.data)
        self.min_val = int('inf')

    def top(self) -> int:
        return self.data[-1] if len(self.data)>0 else None
    def getMin(self) -> int:
        return self.min_val
