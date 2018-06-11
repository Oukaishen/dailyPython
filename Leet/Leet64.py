"""
This is the Leetcode 64
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # row
        M = len(grid)
        # col
        N = len(grid[0])
        
        inf = float("inf")

        # initialize a python list that has one row
        dp = [inf]*N
        dp[0] = 0;
        for i in range(M):
        	for j in range(N):
        		if j == 0:
        			dp[j] += grid[i][0] 
        		else:
        			dp[j] = min(dp[j-1], dp[j]) + grid[i][j]

        return dp[N-1]

