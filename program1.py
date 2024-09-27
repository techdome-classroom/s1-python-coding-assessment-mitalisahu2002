def count_islands(map_grid):
    rows, cols = len(map_grid), len(map_grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    island_count = 0
    
    def dfs(r,c):
        if r < 0 or r>= rows or c<0 or c>= cols or map_grid[r][c] == 'W' or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r-1,c)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r,c+1)
    for r in range(rows):
        for c in range(cols):
            if map_grid[r][c] == 'L' and not visited[r][c]:
                dfs(r,c)
                island_count += 1
    return island_count