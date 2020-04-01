class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        arr = [i for i in range(n)]
        index = 0
        while len(arr) > 1:
            index = index + m - 1
            index = index % len(arr)
            print(arr.pop(index))

        return arr[0]


print(Solution().lastRemaining(n = 10, m = 3))