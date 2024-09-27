class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Check for an empty grid
        if not grid:
            return 0

        # Dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # DFS to visit all land connected to the given cell
        def dfs(r, c):
            # Check if we're out of bounds or at a water cell
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current land cell as visited by turning it into water
            grid[r][c] = 'W'
            # Explore the neighboring cells (up, down, left, right)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # Variable to keep count of islands
        island_count = 0

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If it's an unvisited landmass, start a DFS
                if grid[r][c] == 'L':
                    # Perform DFS to mark all parts of the island as visited
                    dfs(r, c)
                    # Increment the island count
                    island_count += 1

        return island_count

# Function to take user input for the grid
def get_grid_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = []
    print("Enter the grid (L for land, W for water):")
    for _ in range(rows):
        row = input().split()  # Splitting the input row into list elements
        grid.append(row)

    return grid

# Taking input for the grid from the user
user_grid = get_grid_input()

# Creating an instance of the solution class
solution = Solution()

# Printing the result for the user-provided grid
print("Number of islands:", solution.getTotalIsles(user_grid))