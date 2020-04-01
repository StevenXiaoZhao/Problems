class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	prices_len = len(prices)
    	if(prices_len <= 0):
    		return(0)

    	profit=0
    	buy_price = -1
    	sale_price = -1
    	for x in range(1,prices_len):
    		if(buy_price == -1 and prices[x]>prices[x-1]):
    			buy_price = prices[x-1]
    		elif(buy_price != -1 and prices[x]<prices[x-1]):
    			sale_price = prices[x-1]
    			profit += sale_price - buy_price
    			buy_price = -1

    	if(buy_price != -1):
    		profit += prices[prices_len-1] - buy_price

    	return(profit)

ss= Solution()
result = ss.maxProfit([2,1])
print(result)