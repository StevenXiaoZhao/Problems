class MaxQueue:

    def __init__(self):
        self.queue = []
        self.order_queue = []

    def max_value(self) -> int:
        if len(self.queue) == 0:
            return -1
        return self.order_queue[0]

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while len(self.order_queue) > 0 and self.order_queue[-1] < value:
            self.order_queue.pop()

        self.order_queue.append(value)

    def pop_front(self) -> int:
        if len(self.queue) == 0:
            return -1
        if self.order_queue[0] == self.queue[0]:
            self.order_queue.pop(0)

        return self.queue.pop(0)



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()