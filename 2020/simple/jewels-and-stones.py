class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set()
        for s in jewels:
            jewels_set.add(s)

        count = 0
        for s in stones:
            if s in jewels_set:
                count += 1
        return count
    