# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    t = 6
    if num > t:
        return 1
    elif num <t:
        return -1
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        s=1
        e =n
        while e >= s:
            mid = int((s + e) / 2)
            is_num = guess(mid)
            if is_num == 0:
                return mid
            elif is_num == 1:
                e = mid - 1
            else:
                s = mid + 1

print(Solution().guessNumber(10))