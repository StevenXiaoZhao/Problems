from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:

        if chars is None or len(chars) == 0:
            return 0
        elif len(chars) == 1:
            return 1

        count = 0
        curr_count = 1
        j = 0

        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                curr_count += 1
            else:
                temp, j = self.compressWord(chars, j, i - 1, curr_count)
                count += temp
                curr_count = 1

        temp, j = self.compressWord(chars, j, -1, curr_count)
        count += temp

        t = len(chars)
        while t > j:
            chars.pop()
            t -= 1
        return count

    def compressWord(self, chars: List[str], j: int, i: int, curr_count: int) -> (int, int):
        count = 1
        chars[j] = chars[i]
        j += 1
        if curr_count > 1:
            nums = []
            while curr_count > 0:
                count += 1
                nums.append(curr_count % 10)
                curr_count = int(curr_count / 10)
            while len(nums) > 0:
                chars[j] = str(nums.pop())
                j += 1

        return count, j


data = ["a", "a", "b", "b", "c", "c", "c"]
print(Solution().compress(data))
print(data)
