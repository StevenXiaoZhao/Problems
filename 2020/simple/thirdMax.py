from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first_three = set()
        smallest = -100000000000000
        for num in nums:
            if num not in first_three:
                if len(first_three) < 3:
                    first_three.add(num)
                    smallest = min(first_three)

                elif num > smallest:
                    first_three.add(num)
                    first_three.remove(smallest)
                    smallest = min(first_three)

        if len(first_three) == 3:
            return min(first_three)
        else:

            return max(first_three)


print(Solution().thirdMax([1,2,3,4,5,6]))
