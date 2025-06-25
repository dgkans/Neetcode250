class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            #checks/boundary conditions
            if r < 0 or c < 0 or r > n_rows - 1 or c > n_cols - 1:
                return
            #if adjacent node is 0/water then skip
            if grid[r][c] == '0':
                return
            #mark visited nodes as 0
            grid[r][c] = '0'    
            #check adjacent by calling dfs on all 4 adjacent nodes
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        n_rows = len(grid)
        n_cols = len(grid[0])
        count = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count+=1
        return count