def count_islands(map_grid):
    rows, cols = len(map_grid), len(map_grid[0])
    visited = [[False for _ in range(cols)]]