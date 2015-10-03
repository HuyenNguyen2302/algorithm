# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# Algorithmic strategy: Dynamic programming
# One thing to keep in my is the we can perform AT MOST k transactions
# this doesn't mean we have to perform exactly k transactions
# and our top priority is getting the maximum profit
# This means the maximum profit for transaction x could be the same as 
# the maximum profit for transaction (x - 1)  

# Idea: Think about the price difference between day (i + 1) and day i 
# as the "length" of a line segment (the "length" could be negative!)
# Also, use this same idea to visualize the profit in the 2 arrays temp[] and perm[]:
# the array temp[] will keep track of the maximum profit after considering (add/not add) a line segment
# the array perm[] keeps track of the permanent maximum profits for each k value

class Solution:
	# @param {integer} k
	# @param {integer[]} prices
	# @return {integer}
	def maxProfit(self, k, prices):
		numDay = len(prices)

		# Base case: If the number of days is less than 2,
		# then the maximum profit is 0
		if (numDay == 0 or k == 0):
			return 0

		# Other cases:

		# If k >= numDay / 2, then this means we can perform as many transactions as we want
		# Considering the prices for 4 days (a, b, c, d), there are 2 cases:
		# Case 1: a < b < c < d
		# maximum profit = (b - a) + (c - b) + (d - c) = d - a. 
		# Notice: d is the maximum price, a is the minimum price. 
		# Case 2: a < b > c < d
		# maximum profit = (b - a) + (d - c) = (b - c) + (d - a). 
		# This is more than (b - c) or (d - a) alone, 
		# no matter which one (b or d) is the maximum price, and 
		# which one (a or c) is the minimum price
		# The proof can be extended to n days
		if (k >= numDay / 2):
			result = 0
			for i in xrange(1, numDay):
				add = max(prices[i] - prices[i - 1], 0)
				result += add
			return result

		# If k < numDay / 2, use the stategy discussed
		# in the 2nd block of comments (lines 8-12)
		temp = [0 for x in range(k + 1)] # Initialize array with 0s
		perm = [0 for x in range(k + 1)] # Initialize array with 0s
		result = 0 # maximum profit
		for i in xrange(1, numDay):
			for j in xrange(1, k + 1):
				temp[j] = max(temp[j] + prices[i] - prices[i - 1], perm[j - 1]) # read 1st block of comments (lines 1-6)
				perm[j] = max(perm[j], temp[j]) # update the maximum profit for k transactions
				result = max(result, perm[j]) # update maximum profit
		return result