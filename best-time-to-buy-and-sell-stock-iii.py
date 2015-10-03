# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Idea: Using dynamic programming
# Figure out maximum profit after 1st transaction
# by using a for loop in the 'forward direction' (from left to right)
# then, use another for loop in the 'backward direction' (from right to left)
# to figure out maximum after 2nd transaction

class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		numDay = len(prices) # Number of days being considered

		# Base case: If the number of days is less than 2,
		# then the maximum profit is 0
		if (numDay < 2):
			return 0

		# Other cases:
		# For 1st transaction:
		profitTransaction1 = [] # Maximum profit for 1st transaction at day i  
		buyMin1 = prices[0] # Cheapest stock price to buy for 1st transaction
		maxProfit1 = 0 # Maximum profit for 1st transaction
		for i in xrange(0, numDay): # Figure out maximum profit for each day after 1st transaction
			profit = prices[i] - buyMin1
			if (profit > maxProfit1):
				maxProfit1 = profit
			profitTransaction1.append(maxProfit1)
			if (prices[i] < buyMin1):
				buyMin1 = prices[i]
        
        # For 2nd transaction:
		maxProfit2 =  0 # Maximum profit for 2nd transaction
		sellMax2 = prices[numDay - 1] # Highest stock price to sell for 2nd transaction
		for i in range(numDay - 1, -1, -1): # Figure out maximum profit for each day after 2nd transaction
			if (sellMax2 - prices[i] + profitTransaction1[i] > maxProfit2):
				maxProfit2 = sellMax2 - prices[i] + profitTransaction1[i]
			if (prices[i] > sellMax2):
				sellMax2 = prices[i]

		return maxProfit2 # Return maximum profit after 2 transactions




