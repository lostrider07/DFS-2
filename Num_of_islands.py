# Time complexity : O(m * n)   (The actual TC is 2m*n)
# Space complexity : min(m, n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        self.dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, m, n)
                    
        return count
        
        
    def dfs(self, grid, i, j, m, n):
        if (i < 0 or j < 0 or i == m or j == n or grid[i][j] == '0'):
            return
        
        grid[i][j] = '0'
        for dir in self.dirs:
            nr = dir[0] + i
            nc = dir[1] + j
            self.dfs(grid, nr, nc, m, n)
            
