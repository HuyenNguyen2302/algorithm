# Problem: https://leetcode.com/problems/number-of-islands/
# Algorithm: DFS

class Solution:
	# @param grid, a list of list of characters
	# @return an integer
	def numIslands(self, grid):
		# Base case:
		if grid == []:
			return 0

		# Other cases:
		countIsland = 0 # Count number of islands
		rowNum = len(grid) # Number of rows
		columnNum = len(grid[0]) # Number of columns

		# Visit every single point in the given grid
		# if the point is a land, then increment countIsland
		# and perform dfs on the point
		for i in xrange(rowNum):
			for j in xrange(columnNum):
				if grid[i][j] == '1':
					self.dfs(grid, rowNum, columnNum, i, j)
					countIsland += 1
		return countIsland # Return the number of islands
		


	def dfs(self, grid, rowNum, columnNum, i, j):
		# If the point being consider lies outside the grid,
		# don't do anything
		if (i < 0) or (i >= rowNum) or (j < 0) or (j >= columnNum):
			return
		# Otherwise, if the point is land, then change its value to '0'
		# to indicate that it has been visited, and then perform dfs
		# to visit other neighboring points
		else:
			if (grid[i][j] == '1'):
				grid[i][j] = '0'
				self.dfs(grid, rowNum, columnNum, i - 1, j) # Left
				self.dfs(grid, rowNum, columnNum, i + 1, j) # Right
				self.dfs(grid, rowNum, columnNum, i, j - 1) # Above
				self.dfs(grid, rowNum, columnNum, i, j + 1) # Below