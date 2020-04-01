class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.stack_copy = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack_copy.clear()
        count = len(self.stack)
        while count>0:
            self.stack_copy.append(self.stack.pop())
            count -= 1

        self.stack_copy.append(x)
        count = len(self.stack_copy)
        while count>0:
            self.stack.append(self.stack_copy.pop())
            count -= 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stack.pop()
    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack) == 0
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()