def count_islands(map_grid):
    rows, cols = len(map_grid), len(map_grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_count = 0
    
    def dfs(r,c):
        if r < 0 or r>= rows or c<0 or c>= cols or map_grid[r][c]