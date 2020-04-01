from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num1 = 0
        num2 = 0
        numsSet = set(nums)
        for num in numsSet:
            if target - num in numsSet:
                num1 = num
                num2 = target - num

                if num1 == num2:
                    occurs = 0
                    for num in nums:
                        if num == num1:
                            occurs += 1
                    if occurs == 2:
                        break
                    else:
                        num1 = 0
                        num2 = 0
                        continue
                else:
                    break

        num1_index = -1
        num2_index = -1

        for i in range(len(nums)):
            if nums[i] == num1 or nums[i] == num2:

                if num1_index == -1:
                    num1_index = i
                else:
                    num2_index = i
        return [num1_index, num2_index]
test_arr = [217,231,523,52,547,243,648,509,415,149,689,710,265,187,370,56,977,182,400,329,471,805,955,989,255,766,38,566,79,843,295,229,988,108,781,619,704,542,335,307,359,907,727,959,161,699,123,650,147,459,657,188,304,268,405,685,620,721,351,570,899,60,388,771,24,659,425,440,508,373,32,645,409,272,356,175,533,740,370,152,34,510,745,251,227,494,258,527,817,773,178,194,860,387,627,851,449,736,15,212,529,950,316,28,65,484,968,63,4,643,795,669,203,677,139,636,289,555,430,849,150,493,301,377,240,873,965,441,230,349,447,470]

test_target = 718
result = Solution().twoSum(test_arr, test_target)
print(result)