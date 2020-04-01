class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        count = 0
        for num in binary:
            count += int(num)

        return count

print(Solution().hammingWeight(11))
