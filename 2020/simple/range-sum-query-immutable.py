from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = dict()

    def sumRange(self, i: int, j: int) -> int:
        if j-i<=1:
            return sum(self.nums[i:j+1])
        elif i in self.cache:
            k, result1 = self.cache[i]
            if j ==k:
                return result1
            elif j<k and j>k/2:
                return result1-sum(self.nums[j+1:k+1])
            elif j>k:
                result = result1+ sum(self.nums[k+1:j+1])
                self.cache[i] = (j, result)
                return result

        result = sum(self.nums[i:j+1])
        self.cache[i] = (j, result)
        return result

obj = NumArray(nums = [-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)