# Problem: https://leetcode.com/problems/dungeon-game/

class Solution:
	# @param dungeon, a list of lists of integers
	# @return a integer
	def calculateMinimumHP(self, dungeon):
		rowNum = len(dungeon) # Number of rows
		columnNum = len(dungeon[0]) # Number of columns

		# If no 2D array is given, return 0
		if (rowNum == 0 or columnNum == 0):
			return 0

		health = [[0 for x in range(columnNum)] for y in range(rowNum)]

		# Initialize 2D array health[][]
		# This is the array that keeps track of minimum health required
		# to go from the bottom right to the cell at ith row and jth column
		health[rowNum - 1][columnNum - 1] = 1 - min(0, dungeon[rowNum - 1][columnNum - 1])

		# Calculate the minimum health required for each cell
		for i in xrange(rowNum - 2, -1, -1): # For cells in the last column in health[][]
			below = health[i + 1][columnNum - 1]
			if (below - dungeon[i][columnNum - 1] <= 0):
				health[i][columnNum - 1] = 1
			else:
				health[i][columnNum - 1] = below - dungeon[i][columnNum - 1]

		for j in xrange(columnNum - 2, -1, -1): # For cells in the last row in health[][]
			right = health[rowNum - 1][j + 1]
			if (right - dungeon[rowNum - 1][j] <= 0):
				health[rowNum - 1][j] = 1
			else:
				health[rowNum - 1][j] = right - dungeon[rowNum - 1][j]

		for i in xrange(rowNum - 2, -1, -1): # For the remaining cells
			for j in xrange(columnNum - 2, -1, -1):
				right = health[i][j + 1]
				below = health[i + 1][j]
				minHealth = min(right, below)
				if (dungeon[i][j] >= minHealth):
					health[i][j] = 1
				else:
					health[i][j] = minHealth - dungeon[i][j]

		return max(1, health[0][0]) # Return minimum health required to go back to the start