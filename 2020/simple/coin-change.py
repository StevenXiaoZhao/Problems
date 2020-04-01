from typing import List


class Solution:
    def __init__(self):
        self.total_count = float('inf')

    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        return self.coinChangeWithOrdered(coins, 0, 0, amount)

    def coinChangeWithOrdered(self, coins: List[int], coins_index, coins_count, amount: int) -> int:

        if amount == 0:
            return 0

        if coins_index >= len(coins) or amount < coins[-1]:
            return -1

        coin = coins[coins_index]
        coin_max_count = int(amount / coin)
        if coin_max_count + coins_count > self.total_count: #  没有必要进行下去了，因为接下来不管怎么做都只会更大
            return -1

        if amount % coin == 0:
            #print(str(coin) + ':' + str(coin_max_count))
            if coin_max_count + coins_count > self.total_count:
                self.total_count = coin_max_count + coins_count

            return coin_max_count

        if coins_index == len(coins) - 1:
            return -1

        if coin_max_count == 0:
            return self.coinChangeWithOrdered(coins, coins_index + 1, coins_count, amount)

        count = -1
        for i in range(0, coin_max_count+1):
            rest = self.coinChangeWithOrdered(coins, coins_index + 1, coins_count + coin_max_count - i, amount - coin * (coin_max_count - i))
            result = rest + coin_max_count - i
            if rest != -1 and (count == -1 or result <= count):
                count = result
                #print(str(coin) + ':' + str(count))

            #if rest != -1 and 0 <= count < result:
            #    break
        return count


print(Solution().coinChange([282,116,57,239,103,89,167],4856))
