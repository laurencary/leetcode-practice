from collections import deque
def count_paths(grid):
  if grid[len(grid) - 1][len(grid[0]) - 1] == "X": return 0
  return _count_paths(grid, 0, 0, {})

def _count_paths(grid, r, c, memo):
  if r == len(grid) - 1 and c == len(grid[0]) - 1: return 1
  if (r, c) in memo: return memo[(r, c)]
  if grid[r][c] == "X": return 0
  left_path, right_path = 0, 0
  if inbounds(grid, r, c + 1):
    left_path = _count_paths(grid, r, c + 1, memo)
  if inbounds(grid, r + 1, c):
    right_path = _count_paths(grid, r + 1, c, memo)

  memo[(r, c)] = right_path + left_path
  return memo[(r, c)]


def inbounds(grid, r, c):
  row_in = 0 <= r < len(grid)
  col_in = 0 <= c < len(grid[0])
  return row_in and col_in

grid = [
  ["O", "O", "O"],
  ["O", "O", "X"],
  ["O", "O", "O"],
]
print(count_paths(grid)) # -> 2