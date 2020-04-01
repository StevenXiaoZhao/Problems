import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # m*(m-1)/2<=n,求m最大值
        m = int((math.sqrt(8*n+1)-1)/2)
        return m

print(Solution().arrangeCoins(0))