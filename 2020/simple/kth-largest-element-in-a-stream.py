from typing import List
import heapq


class KthLargest:
    k = 0
    nums = []

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        n = len(self.nums)
        while n > k:
            n -= 1
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappush(self.nums, val)
            heapq.heappop(self.nums)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


kthLargest = KthLargest(3, [5, -1])
print(kthLargest.add(2))   # return 4
print(kthLargest.add(1)) # return 5
print(kthLargest.add(-1)) # return 5
print(kthLargest.add(3)) # return 8
print(kthLargest.add(4))   # return 8
